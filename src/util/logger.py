import logging
from colorlog import ColoredFormatter

LOGFORMAT = "  %(log_color)s%(levelname)-8s%(reset)s | %(log_color)s%(message)s%(reset)s"


def init_logger(log_level: int, logger_name: str = "pythonConfig") -> logging.Logger:
    logging.root.setLevel(log_level)
    formatter = ColoredFormatter(LOGFORMAT)
    stream = logging.StreamHandler()
    stream.setLevel(log_level)
    stream.setFormatter(formatter)
    logger = logging.getLogger(logger_name)
    logger.setLevel(log_level)
    logger.addHandler(stream)

    return logger
