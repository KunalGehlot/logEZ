# logEZ
Make logging easy in your applications! Use this simple library to easily use logs in any of your applications.

# How to run

```python
from logEZ import MyLogger

logger = MyLogger()
```
## `MyLogger()`

The `init` method of class MyLogger takes four default arguments. 
`log_file_name`, `logging_level`, `disable_console_logs` and `disable_file_logs`

The default values are
```python
log_file_name="logEZ.log",
logging_level="INFO",
disable_console_logs=False,
disable_file_logs=False
```

- `log_file_name`

    You can specify the file name of your log file here.

- `logging_level`

    You can specify the default logging level of your logs.

    It can be `INFO`, `DEBUG`, `WARNING`, `ERROR` or `CRITICAL`

- `disable_console_logs`

    This disables the console logging of your logs, if set `True`.

- `disable_file_logs`

    This disables the file logging of your logs, if set `True`.

## Methods
Once you have an object initialized, you can use the following methods.

 - `setLoggingLevel(level)`: To change the logging level after initializing `MyLogger()`. (Refer `logging_level` under `MyLogger()` for levels)
 - `myDebug(str)`: To print a `debug` log. Accepts string input.
 - `myInfo(str)`: To print an `info` log. Accepts string input.
 - `myWarn(str)`: To print a `warning` log. Accepts string input.
 - `myError(str, exc_info[Optional])`: To print an `error` log. Accepts string input. If `exc_info` is set `True`, it appends complete execution information along with the log string.
 - `myCrit(strm exc_info[Optional])`: To print an `error` log. Accepts string input. If `exc_info` is set `True`, it appends complete execution information along with the log string.
 - `myExcept(str)`: To print an `exception` log. Accepts string input.
