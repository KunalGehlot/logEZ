"""Formatters for logEZ: Custom formatters for console and file logging."""

import logging
from logging import Formatter


def get_default_formatter() -> Formatter:
    """Create and return the default formatter for logEZ.

    The default formatter has the following format:
    '%(asctime)s - %(name)s : %(levelname)s : %(message)s'
    with a date format of '%d-%m-%y %H:%M:%S'.

    Returns:
        Formatter: The configured default formatter.
    """
    log_format = "%(asctime)s - %(name)s : %(levelname)s : %(message)s"
    date_format = "%d-%m-%y %H:%M:%S"
    formatter = logging.Formatter(log_format, date_format)
    return formatter
