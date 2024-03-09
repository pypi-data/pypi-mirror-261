#!/usr/bin/env python3
"""TCP/UDP proxy for NetGDB. Translates between Debugnet UDP GDB packets from a
panicked kernel and TCP GDB packets from a client."""

import argparse
import daemon
import multiprocessing

from . import logger
from .herald_listener import HeraldListener
from .logger import LOG
from .proxy import NetGDB_Proxy


def run():
    parser = argparse.ArgumentParser(
        description="NetGDB Proxy. Allows GDB debugging on a paniced kernel "
        "over the network."
    )
    logger.get_log_args(parser)
    args = parser.parse_args()
    logger.parse_log_args(args)

    LOG.info("Starting in daemon mode.")
    with daemon.DaemonContext():
        herald_listener = HeraldListener(True)
        while True:
            # Wait for debugnet connection
            debugnet_addr = herald_listener.listen()
            proxy = NetGDB_Proxy(True, None, False)
            proxy_process = multiprocessing.Process(
                target=proxy.run, args=[debugnet_addr]
            )
            proxy_process.start()
