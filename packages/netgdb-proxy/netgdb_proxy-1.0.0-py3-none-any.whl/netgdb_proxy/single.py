#!/usr/bin/env python3
"""TCP/UDP proxy for NetGDB. Translates between Debugnet UDP GDB packets from a
panicked kernel and TCP GDB packets from a client."""

import argparse

from . import logger
from .herald_listener import HeraldListener
from .logger import LOG
from .proxy import NetGDB_Proxy


def run():
    # Parse args and set up port numbers
    parser = argparse.ArgumentParser(
        description="NetGDB Proxy. Allows GDB debugging on a paniced kernel "
        "over the network."
    )
    logger.get_log_args(parser)
    parser.add_argument(
        "-P",
        "--profile",
        action="store_true",
        help="Generate performance profile of communication timings.",
    )
    parser.add_argument(
        "-p", "--port", type=int, help="Single proxy GDB client listen port.", default=0
    )
    parser.add_argument(
        "-q", "--quiet", action="store_true", help="Silences print messages."
    )
    args = parser.parse_args()
    logger.parse_log_args(args)

    LOG.info("Starting in single mode.")
    herald_listener = HeraldListener(args.quiet)
    proxy = NetGDB_Proxy(args.quiet, args.port, args.profile)
    try:
        debugnet_addr = herald_listener.listen()
        herald_listener.exit()
        proxy.run(debugnet_addr)
    except KeyboardInterrupt:
        herald_listener.exit()
        proxy.exit()
    LOG.info("Exiting single mode.")
