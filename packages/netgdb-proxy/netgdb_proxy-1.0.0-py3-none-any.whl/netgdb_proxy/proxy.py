import asyncio
import signal
import socket
import sys

from . import util
from .logger import LOG
from .profiler import Profiler


class NetGDB_Proxy:
    def __init__(self, quiet, port, profile) -> None:
        self.debugnet_addr = None
        self.debugnet_socket = None
        self.seqno = 1

        self.client_addr = None
        self.client_port = port
        self.client_socket = None

        # Retry sending unacked packets
        self.debugnet_unacked_packets = {}
        self.retries = 0
        self.send_timestamp = None

        self.quiet = quiet
        self.profiler = Profiler() if profile else None

        self.setup_sockets()

    def output(self, message):
        if not self.quiet:
            print(message)

    def exit(self):
        """Close sockets and connections and exit."""
        LOG.info("Proxy shutting down.")
        self.output("Proxy shutting down.")
        if self.debugnet_socket:
            self.debugnet_socket.close()
        if self.client_socket:
            self.client_socket.close()
        if self.profiler:
            self.profiler.finalize()
        sys.exit(0)

    def stop_loop(self):
        loop = asyncio.get_running_loop()
        loop.remove_reader(self.debugnet_socket)
        loop.remove_reader(self.client_socket)
        loop.stop()

    def setup_sockets(self):
        """Set up both udp and tcp ports for proxy operations."""
        dbn_sock = util.get_dbn_socket()
        tcp_sock = util.get_tcp_socket()

        while True:
            try:
                dbn_sock.bind(("", 0))
            except socket.error:
                continue

            udp_port = dbn_sock.getsockname()[1]
            tcp_port = self.client_port if self.client_port else udp_port + 1

            try:
                tcp_sock.bind(("", tcp_port))
            except socket.error:
                if self.client_port:
                    msg = (
                        "Could not bind to tcp port %d, most likely already in use."
                        " Check running processes and try again." % self.client_port
                    )
                    LOG.error(msg)
                    self.output(msg)
                    dbn_sock.close()
                    tcp_sock.close()
                    sys.exit(1)
                continue

            break

        self.debugnet_socket = dbn_sock
        self.client_socket = tcp_sock

    def debugnet_connect(self, debugnet_addr):
        """Establish connection with NetGDB on debugnet"""
        self.debugnet_addr = debugnet_addr

        # Send initial Ack for herald, which has the side effect of informing
        # NetGDB of the new port.
        self.debugnet_socket.connect(self.debugnet_addr)
        self.debugnet_socket.setblocking(0)
        print("Connection from NetGDB at %s received." % self.debugnet_addr[0])

    def client_connect(self):
        """Wait for a client TCP connection."""
        self.client_socket.listen(1)
        if not self.quiet:
            bound_port = self.client_socket.getsockname()[1]
            self.output(
                f"Use 'target remote <this machine's ip>:{bound_port}'"
                " from gdb to connect."
            )
        self.client_socket, self.client_addr = self.client_socket.accept()
        self.output("Connection from GDB client received.")
        self.client_socket.setblocking(0)

    def send_to_client(self, data):
        """Send a data chunk to the client over tcp."""
        self.client_socket.send(data)
        LOG.debug(f"Sent message {data.decode()} to client.")
        if self.profiler:
            self.profiler.record_send("client", data.decode())

    def send_to_debugnet(self, data):
        """Send a data chunk to the debugnet over udp."""
        self.debugnet_socket.send(data)
        if self.profiler:
            self.profiler.record_send("debugnet", data)

        LOG.debug(
            f"Sent message {data.decode()} to "
            f"{':'.join(map(str, self.debugnet_addr))}, "
            f"expecting acks: {list(self.debugnet_unacked_packets)}"
        )

    def debugnet_data_handler(self):
        """Takes data received from debugnet's NetGDB and forwards it to the client."""
        data = self.debugnet_socket.recv(util.RX_BUFFER_SIZE)
        if not data:
            return
        self.send_to_client(data)
        if self.profiler:
            self.profiler.record_receive("debugnet")

    def client_data_handler(self):
        """Takes data received from client and forwards it to the debugnet."""
        # Reset our retries as the client is probably retrying too
        self.debugnet_socket.reset_unacked_packets()
        try:
            # Both failing to recv and successfully empty receive (End of
            # Stream) are a Connection reset error.
            data = self.client_socket.recv(util.RX_BUFFER_SIZE)
            if not data:
                raise ConnectionResetError()
        except ConnectionResetError:
            LOG.info("Client connection lost. Exiting proxy.")
            self.output("Client connection lost. Exiting proxy.")
            self.stop_loop()
            return

        LOG.debug(f"Received data from client: {data.decode()}")
        if self.profiler:
            self.profiler.record_receive("client")
        self.send_to_debugnet(data)

    def eventloop(self):
        """
        ### Main Loop ###
        Currently assuming that the connection between client and server will be
        half-duplex, i.e. only one talks at a time.

        When a client message is received, it is cut into debugnet packets, prepends
        debugnet headers to them, and sends them to the debugnet. We then expect acks
        from the debugnet for every packet sent, and resend unacked packets, mimicking
        TCP.

        When a server message is received, we ack it, cut the debugnet header off, and
        forward it to the client.
        """
        self.output("Starting proxy. Press ctrl-C to stop.")
        loop = asyncio.new_event_loop()
        loop.add_reader(self.debugnet_socket, self.debugnet_data_handler)
        loop.add_reader(self.client_socket, self.client_data_handler)
        resend_task = loop.create_task(self.debugnet_socket.get_resend_task())
        loop.add_signal_handler(signal.SIGINT, lambda: loop.stop())
        try:
            loop.run_forever()
        finally:
            resend_task.cancel()
            loop.run_until_complete(resend_task)
            loop.close()
            self.exit()

    def run(self, debugnet_addr):
        # Get connection from debugnet and client
        self.debugnet_connect(debugnet_addr)
        self.client_connect()
        LOG.debug(
            "Connections made. Debugnet: %s. GDB: %s"
            % (
                ":".join(map(str, self.debugnet_addr)),
                ":".join(map(str, self.client_addr)),
            )
        )

        self.eventloop()
