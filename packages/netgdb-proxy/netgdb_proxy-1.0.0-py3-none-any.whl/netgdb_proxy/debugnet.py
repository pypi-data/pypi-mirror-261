import struct

DBN_HDR_FORMAT = ">IIQII"
DBN_ACK_FORMAT = ">I"
DEBUGNET_HDR_SIZE = struct.calcsize(DBN_HDR_FORMAT)
DEBUGNET_ACK_SIZE = struct.calcsize(DBN_ACK_FORMAT)

DEBUGNET_MAX_IN_FLIGHT = 64
DBN_RETRIES = 10

HERALD_PORT = 20025

DEBUGNET_HERALD = 1
DEBUGNET_FINISHED = 2
DEBUGNET_DATA = 3


class debugnet_msg_hdr:
    def __init__(self, data=None):
        self.size = DEBUGNET_HDR_SIZE
        if not data:
            self.type = DEBUGNET_HERALD
            self.seqno = 0
            self.offset = 0
            self.length = 0
            self.aux2 = 0
        else:
            self.type, self.seqno, self.offset, self.length, self.aux2 = struct.unpack(
                DBN_HDR_FORMAT, data[:DEBUGNET_HDR_SIZE]
            )

    def to_bytearray(self):
        return struct.pack(
            DBN_HDR_FORMAT, self.type, self.seqno, self.offset, self.length, self.aux2
        )

    def to_ack(self):
        return struct.pack(DBN_ACK_FORMAT, self.seqno)


def get_ack_seqno(data: bytes) -> int:
    return struct.unpack(DBN_ACK_FORMAT, data)[0]


def packet_is_ack(data: bytes) -> bool:
    return len(data) == DEBUGNET_ACK_SIZE


def packet_is_runt(data: bytes) -> bool:
    return len(data) < DEBUGNET_HDR_SIZE


def get_data_contents(data: bytes) -> bytes:
    hdr = debugnet_msg_hdr(data)
    data = data[hdr.size :]  # cut off header
    return data, hdr.seqno


def get_ack(seqno: int):
    return struct.pack(DBN_ACK_FORMAT, seqno)


def create_data_packet(
    data: bytes, seqno: int, packet_start: int, packet_len: int
) -> bytes:
    hdr = debugnet_msg_hdr()
    hdr.type = DEBUGNET_DATA
    hdr.seqno = seqno
    hdr.offset = packet_start
    hdr.length = packet_len

    # Package and send data
    packet = hdr.to_bytearray() + data[packet_start : packet_start + packet_len]
    return packet
