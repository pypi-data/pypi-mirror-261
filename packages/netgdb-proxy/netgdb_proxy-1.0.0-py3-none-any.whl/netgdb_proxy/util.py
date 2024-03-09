import asyncio
import socket

from . import debugnet as dbn
from . import debugnet_socket

MTU = 1500

# Accept arbitrarily large UDP packets from the network stack.
# (INET and INET6 both have 16 bit max payload sizes.)
#
# The constant is reused for non-blocking TCP recv as well; there, it
# is just an arbitrary value.
RX_BUFFER_SIZE = 2**16

# There are three limiting factors to the size of packets we can send.
#
# GDB packets can be as large as GDB_BUFSZ + 4 for $#.. - 1 for the null byte. The
# largest supported GDB_BUFSZ is 4096 bytes, so we theoretically can receive 4099-byte
# GDB packets. GDB will control this via the PacketSize message, so we won't ever be
# asked to send an oversize packet.
#
# We also need to constrain to mbuf cluster sizes, which are set in network
# drivers' debugnet_init functions. The minimum value is MCLBYTES, or 2048 bytes.
#
# Finally, we need to constrain to MTU limitations. Debugnet does not support
# fragmentation, so we need to keep packets under the typical MTU of 1500 bytes. While
# many platforms support jumbo (9k) MTUs, some do not (AWS), so our packets need to be
# 1500 bytes or under.
#
# As there is a chance we will receive GDB packets larger than nics are able to accept,
# (4099-byte packets that need to fit in to a 1500-byte MTU) we need to be able to split
# incoming packets from the client. Each packet needs a debugnet header.
#
# So max payload size is 1500 - ip header - udp header - debugnet header.
TX_PAYLOAD_SIZE = MTU - 20 - 8 - dbn.DEBUGNET_HDR_SIZE


def get_socket(socket_type):
    sock = socket.socket(socket.AF_INET, socket_type)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setblocking(1)
    return sock


def get_udp_socket():
    return get_socket(socket.SOCK_DGRAM)


def get_dbn_socket():
    sock = debugnet_socket.DebugnetSocket()
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.setblocking(1)
    return sock


def get_tcp_socket():
    return get_socket(socket.SOCK_STREAM)


async def every(seconds, func, *args, **kwargs):
    while True:
        func(*args, **kwargs)
        try:
            await asyncio.sleep(seconds)
        except asyncio.CancelledError:
            break
