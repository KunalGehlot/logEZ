"""Handlers for logEZ: Custom handlers for console and file logging."""

import logging
from logging import FileHandler, StreamHandler, Formatter


def get_console_handler(formatter: Formatter) -> StreamHandler:
    """Create and return a console handler with the specified formatter.

    Args:
        formatter (Formatter): The formatter to use for the console handler.

    Returns:
        StreamHandler: The configured console handler.
    """
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    return console_handler


def get_file_handler(log_file_name: str, formatter: Formatter) -> FileHandler:
    """Create and return a file handler with the specified formatter and log file name.

    Args:
        log_file_name (str): The name of the log file to write logs to.
        formatter (Formatter): The formatter to use for the file handler.

    Returns:
        FileHandler: The configured file handler.
    """
    file_handler = logging.FileHandler(log_file_name)
    file_handler.setFormatter(formatter)
    return file_handler
