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
* `myExcept(inString: str)`: Log an exception message. Accepts a string input.

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