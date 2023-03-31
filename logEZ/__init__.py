"""logEZ: A simple, easy-to-use logging library for Python applications."""

from .mylogger import MyLogger
from .handlers import get_console_handler, get_file_handler
from .formatters import get_default_formatter

__all__ = [
    "MyLogger",
    "get_console_handler",
    "get_file_handler",
    "get_default_formatter",
]
