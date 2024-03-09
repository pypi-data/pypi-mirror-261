import logging
import signal
import time


class Profiler:
    def __init__(self):
        self.dbn_total_resp_time = 0
        self.client_total_resp_time = 0
        self.send_time = None
        self.message = None
        self.recipient = None
        signal.signal(signal.SIGINT, self.exit_handler)

    def record_send(self, recipient, message):
        if recipient not in {"debugnet", "client"}:
            raise ValueError(
                "profiler: recipient must be either 'debugnet' or " "'client'."
            )
        self.send_time = time.time()
        self.message = message
        self.recipient = recipient

    def record_receive(self, recipient):
        if not self.send_time:
            return
        response_time = time.time() - self.send_time
        if recipient != self.recipient:
            logging.debug(f"Received multiple sequential packets from {recipient}")
            return
        if response_time > 1.0:
            logging.debug(
                "%s responded in %f\nDelayed packet: %s"
                % (recipient, response_time, repr(self.message))
            )
        if self.recipient == "debugnet":
            self.dbn_total_resp_time += response_time
        else:
            self.client_total_resp_time += response_time

    def finalize(self):
        if self.dbn_total_resp_time and self.client_total_resp_time:
            logging.debug(
                "Total time waiting for debugnet: %f" % self.dbn_total_resp_time
            )
            logging.debug(
                "Total time waiting for client (includes user response "
                "time): %f" % self.client_total_resp_time
            )
