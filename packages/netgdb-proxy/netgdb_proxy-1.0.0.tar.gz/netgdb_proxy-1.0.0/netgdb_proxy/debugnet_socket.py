import asyncio
import socket
import time
from typing import Union

from . import debugnet as dbn
from . import util
from .logger import LOG

POLL_DELAY = 0.2


class DebugnetSocket(socket.socket):
    def __init__(self, proto=-1, fileno=None) -> None:
        super().__init__(socket.AF_INET, socket.SOCK_DGRAM, proto, fileno)

        self.unacked_packets = {}
        self.seqno = 0
        self.retries = 0

    def connect(self, __address) -> None:
        super().connect(__address)
        ack = dbn.get_ack(1)
        LOG.debug("Sending herald ack.")
        super().send(ack)

        # Get and ack the T packet from debugnet
        #
        # This is a kludge based on the current initial $T packet blasted out by
        # FreeBSD's gdb stub for inexplicable reasons (GDB is a debugger-driven
        # interrogation protocol; sending first makes no sense).
        while True:
            data = self.recv(util.RX_BUFFER_SIZE)
            if data[:2] == b"$T":
                LOG.debug(f"Received T packet: {data.decode()}")
                break
            LOG.debug("Received non-T packet from debugnet")

    def recv(self, __bufsize: int, __flags: int = 0) -> Union[bytes, None]:
        data = super().recv(__bufsize, __flags)

        if dbn.packet_is_ack(data):
            self._handle_ack(data)
        else:
            return self._get_message(data)

    def _get_message(self, data):
        if dbn.packet_is_runt(data):
            LOG.warning("Got runt packet from NetGDB: %d bytes" % len(data))
            return

        # Received a data packet from debugnet, ack and forward to client
        message, seqno = dbn.get_data_contents(data)

        LOG.debug(
            f"Received debugnet data: {message.decode()}, sending data ack: {seqno}"
        )
        ack_msg = dbn.get_ack(seqno)
        super().send(ack_msg)
        return message

    # Handle an ACK from NetGDB.
    def _handle_ack(self, data):
        """Registers acks from the debugnet. Unacked packets will get resent."""
        ack_seqno = dbn.get_ack_seqno(data)
        LOG.debug(f"Received udp ack {ack_seqno}.")

        if ack_seqno not in self.unacked_packets:
            # Ignore unneeded or spurious ack
            LOG.debug(f"Received spurious ack, ignoring: {ack_seqno}")
            return

        # Packet is a current ack.
        del self.unacked_packets[ack_seqno]

        if not self.unacked_packets:
            LOG.debug("Found all acks for all packets sent.")

    def send(self, __data, __flags: int = 0) -> int:
        """Send a data chunk to the debugnet over udp."""
        datalen = len(__data)
        for pkt_start in range(0, datalen, util.TX_PAYLOAD_SIZE):
            self.seqno += 1
            pktlen = min(datalen - pkt_start, util.TX_PAYLOAD_SIZE)

            # Set up header information
            packet = dbn.create_data_packet(__data, self.seqno, pkt_start, pktlen)
            super().send(packet, __flags)

            # Note that we're waiting for this packet and record a copy for retransmit.
            self.unacked_packets[self.seqno] = packet

        self.send_timestamp = time.time()

    def reset_unacked_packets(self):
        """Reset unacked packets, retry count, and resend timestamp."""
        self.retries = 0
        self.send_timestamp = time.time()
        self.unacked_packets.clear()

    def _resend_unacked_packets(self):
        """If not all packets have come in after a while, try resending."""

        if self.unacked_packets and time.time() - self.send_timestamp > 0.1:
            LOG.error("Not all acks received. Resending packet(s).")

            if self.retries >= dbn.DBN_RETRIES:
                LOG.error("Out of retries!  Assuming connectivity lost.")
                asyncio.get_running_loop().stop()

            for k in sorted(self.unacked_packets.keys()):
                LOG.debug("Resending seqno %d to NetGDB.", k)
                self.send(self.unacked_packets[k])

            self.retries += 1

    def get_resend_task(self):
        return util.every(POLL_DELAY, self._resend_unacked_packets)

    def close(self) -> None:
        try:
            self.getpeername()
            finisher = dbn.debugnet_msg_hdr()
            finisher.type = dbn.DEBUGNET_FINISHED
            super().send(finisher.to_bytearray())
        except Exception:
            pass
        return super().close()
