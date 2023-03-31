"""logEZ: A simple, easy-to-use logging library for Python applications."""

import logging
from typing import Dict
from .handlers import get_console_handler, get_file_handler
from .formatters import get_default_formatter


root_logger = logging.getLogger()


class MyLogger:
    """A simple logging class that wraps around the
    standard Python logging library.

    Attributes:
        logging_levels (Dict[str, int]): A dictionary mapping
        logging level names to their respective logging level values.
    """

    def __init__(
        self,
        log_file_name: str = "logEZ.log",
        logging_level: str = "INFO",
        disable_console_logs: bool = False,
        disable_file_logs: bool = False,
    ) -> None:
        """Initialize the MyLogger instance.

        Args:
            log_file_name (str, optional): Name of the log file to write logs to. # noqa: E501
            Defaults to 'logEZ.log'.
            logging_level (str, optional): The initial logging level. # noqa: E501
            Defaults to 'INFO'.
            disable_console_logs (bool, optional): If True, disable logging to the console. # noqa: E501
            Defaults to False.
            disable_file_logs (bool, optional): If True, disable logging to the file. # noqa: E501
            Defaults to False.

        Raises:
            ValueError: Both console and file logs are disabled.
            ValueError: Invalid logging level.
        """

        if disable_console_logs and disable_file_logs:
            raise ValueError("Both console and file logs are disabled")

        self.logging_levels: Dict[str, int] = {
            "INFO": logging.INFO,
            "DEBUG": logging.DEBUG,
            "WARNING": logging.WARNING,
            "ERROR": logging.ERROR,
            "CRITICAL": logging.CRITICAL,
        }

        try:
            log_level = self.logging_levels[logging_level]
        except KeyError as exc:
            raise ValueError(
                f"Invalid logging level: {logging_level}"
            ) from exc

        log_formatter = get_default_formatter()

        root_logger.setLevel(log_level)

        if not disable_file_logs:
            file_handler = get_file_handler(log_file_name, log_formatter)
            root_logger.addHandler(file_handler)

        if not disable_console_logs:
            console_handler = get_console_handler(log_formatter)
            root_logger.addHandler(console_handler)

        self.debug("logEZ initialized...")

    def set_logging_level(self, level: str) -> None:
        """Set the logging level.

        Args:
            level (str): The new logging level.

        Raises:
            ValueError: Invalid logging level.
        """
        try:
            log_level = self.logging_levels[level]
        except KeyError as exc:
            raise ValueError(f"Invalid logging level: {level}") from exc
        root_logger.setLevel(log_level)

    def debug(self, in_string: str) -> None:
        """Log a debug message.

        Args:
            in_string (str): The debug message to log.
        """
        root_logger.debug(in_string)

    def info(self, in_string: str) -> None:
        """Log an info message.

        Args:
            in_string (str): The info message to log.
        """
        root_logger.info(in_string)

    def warning(self, in_string: str) -> None:
        """Log a warning message.

        Args:
            in_string (str): The warning message to log.
        """
        root_logger.warning(in_string)

    def error(self, in_string: str, exc_info: bool = False) -> None:
        """Log an error message.

        Args:
            in_string (str): The error message to log.
            exc_info (bool, optional): If True, include exception
            information in the log. Defaults to False.
        """
        root_logger.error(in_string, exc_info=exc_info)

    def critical(self, in_string: str, exc_info: bool = False) -> None:
        """Log a critical message.

        Args:
            in_string (str): The critical message to log.
            exc_info (bool, optional): If True, include exception
            information in the log. Defaults to False.
        """
        root_logger.critical(in_string, exc_info=exc_info)
