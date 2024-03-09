import logging
import logging.handlers
import pathlib

LOG_PATH = None
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DEFAULT_LOG_LEVEL = logging.WARN
MAX_LOG_SIZE = 100 * 1024**2
LOG_BACKUPS = 3


def get_logger(log_level=DEFAULT_LOG_LEVEL, path=LOG_PATH):
    logger = logging.Logger(__file__, log_level)
    formatter = logging.Formatter(LOG_FORMAT)
    if path:
        handler = logging.handlers.RotatingFileHandler(
            LOG_PATH, maxBytes=MAX_LOG_SIZE, backupCount=LOG_BACKUPS
        )
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    return logger


def set_log_level(level):
    LOG.setLevel(level)


def get_log_args(parser):
    logging_group = parser.add_mutually_exclusive_group()
    logging_group.add_argument(
        "-l",
        "--log-level",
        type=int,
        help="Set logging level.",
        default=DEFAULT_LOG_LEVEL,
    )
    logging_group.add_argument(
        "-d",
        "--debug",
        action="store_const",
        help="Log debug messages.",
        dest="log_level",
        const=logging.DEBUG,
    )
    parser.add_argument(
        "--log-path",
        type=pathlib.Path,
        help="Where to log to.",
    )


def parse_log_args(args):
    set_log_level(args.log_level)


LOG = get_logger()
