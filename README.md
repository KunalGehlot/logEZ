# logEZ

Make logging easy in your applications! Use this simple library to easily use logs in any of your applications.

## Installation

```bash
pip install logEZ
```

## How to use

```python
from logEZ import MyLogger

logger = MyLogger()
```

More in [Sample App](./sample_app.md)

### `MyLogger` class

The __init__ method of the MyLogger class takes four optional arguments:

* `log_file_name`
* `logging_level`
* `disable_console_logs`
* `disable_file_logs`

The default values are:

```python
log_file_name="logEZ.log",
logging_level="INFO",
disable_console_logs=False,
disable_file_logs=False
```

* `log_file_name`: Specify the file name of your log file here.
* `logging_level`: Specify the default logging level of your logs. It can be `INFO`, `DEBUG`, `WARNING`, `ERROR`, or `CRITICAL`.
* `disable_console_logs`: Disable the console logging of your logs, if set to `True`.
* `disable_file_logs`: Disable the file logging of your logs, if set to `True`.

### `MyLogger` methods

Once you have initialized a MyLogger object, you can use the following methods:

* `setLoggingLevel(level: str)`: Change the logging level after initializing `MyLogger()`. (Refer to logging_level under [`MyLogger` class](#mylogger-class) for levels.)
* `debug(inString: str)`: Log a `DEBUG` level message. Accepts a string input.
* `info(inString: str)`: Log an `INFO` level message. Accepts a string input.
* `warning(inString: str)`: Log a `WARNING` level message. Accepts a string input.
* `error(inString: str, exc_info: Optional[bool] = False)`: Log an `ERROR` level message. Accepts a string input. If `exc_info` is set to True, it appends the complete execution information along with the log string.
* `critical(inString: str, exc_info: Optional[bool] = False)`: Log a `CRITICAL` level message. Accepts a string input. If `exc_info` is set to True, it appends the complete execution information along with the log string.

#### Using `exc_info` to send complete execution information

The `exc_info` parameter is an optional argument available in the `error` and `critical` methods of the `MyLogger` class. When set to `True`, it appends the complete execution information, including the traceback, along with the log message. This can be particularly useful when debugging errors or critical issues that require detailed information about the context in which they occurred.

Here's an example of how to use the `exc_info` parameter with myError and `critical` methods:

```python
from logEZ import MyLogger

logger = MyLogger()

def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError as e:
        logger.myError(f"An error occurred while dividing {a} by {b}", exc_info=True)
        return None
    return result

divide(10, 0)
```

In this example, we have a `divide` function that takes two numbers as arguments and attempts to perform a division operation. If a `ZeroDivisionError` exception is raised, the `error` method is called with the `exc_info` parameter set to `True`. This will log the error message along with the complete execution information, including the traceback, making it easier to understand the context in which the error occurred.

The output of this code will be:

```bash
01-04-23 14:35:28 - root : ERROR : An error occurred while dividing 10 by 0
Traceback (most recent call last):
  File "example.py", line 7, in divide
    result = a / b
ZeroDivisionError: division by zero
```

Similarly, you can use the `exc_info` parameter with the `critical` method if you want to log critical messages with complete execution information.

## Why use logEZ?

The logEZ library provides a simplified interface to work with the standard logging module in Python. While it does not introduce any new functionality or significant improvements over the built-in logging module, it may be helpful for developers who want a more straightforward, easy-to-use API for common logging tasks.

Advantages of logEZ:

1. Simplified initialization: The logEZ library makes it easier to set up logging with default values and simple customization options. You can easily configure log file names, logging levels, and toggle console or file logging with just a few parameters.
2. Unified logging methods: The logEZ library offers a single class, MyLogger, with methods for different logging levels (debug, info, warning, error, critical), making it more convenient to use compared to the standard logging module, which requires calling separate functions for each logging level.
3. Easier traceback logging: The logEZ library provides the exc_info parameter for error and critical level logs, making it more straightforward to include traceback information when logging exceptions.

However, for more advanced logging use cases or if you require fine-grained control over your logging configuration, the built-in logging module offers more comprehensive features and flexibility. If you are already familiar with the standard logging module, you may not find logEZ to be significantly more helpful.

In summary, the logEZ library can be useful for developers looking for a simpler and more accessible interface for basic logging tasks. However, it might not offer substantial advantages over the built-in logging module for more experienced users or advanced logging scenarios.

## What's next?

We have some exciting plans for the future development of logEZ, and we're always looking for ways to make it even more useful for our users. Here's a list of features we're considering adding:

1. Configuration from file support
2. Log rotation functionality
3. Support for custom log handlers
4. Colored console logs
5. Enhanced context information in log messages
6. Improved exception handling and logging
7. Integrated performance metrics
8. Advanced filtering capabilities
9. Asynchronous logging support
10. Better documentation and examples

_We're open to contributions!_ If you'd like to help implement any of these features or have suggestions for improvements, please feel free to reach out to us. You can contact us at [gehlotkunal@outlook.com](mailto:gehlotkunal@outlook.com) or connect with us on Twitter at [@ZackCodesAI](https://twitter.com/ZackCodesAI).

We're looking forward to collaborating with the community to make logEZ an even more valuable and versatile logging library for Python developers!
