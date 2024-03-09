import socket
import sys

from . import debugnet as dbn
from .logger import LOG
from . import util


class HeraldListener:
    def __init__(self, quiet) -> None:
        self.quiet = quiet
        self.sock = None
        self.setup_socket()

    def setup_socket(self):
        sock = util.get_udp_socket()

        try:
            sock.bind(("", dbn.HERALD_PORT))
        except socket.error:
            LOG.error(
                "Could not bind to herald port %d, most likely already in use."
                "Check running processes and try again." % dbn.HERALD_PORT
            )
            self.exit()
            sys.exit()

        # TODO: enumerate machine interfaces via something like ioctl and print
        # possibilities.
        if not self.quiet:
            print(
                "Waiting for connection from NetGDB client.\n"
                "Use 'netgdb -s <this machine's ip>' at the 'db>' prompt to connect."
            )

        self.sock = sock

    def listen(self):
        message_header = None
        while True:
            data, debugnet_addr = self.sock.recvfrom(util.RX_BUFFER_SIZE)
            if dbn.packet_is_runt(data):
                continue
            message_header = dbn.debugnet_msg_hdr(data)
            if message_header.type == dbn.DEBUGNET_HERALD:
                break
        LOG.debug(f"Received herald from {debugnet_addr}")
        return debugnet_addr

    def exit(self):
        self.sock.close()
