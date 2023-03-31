# Sample App

```python
from logEZ import MyLogger
import os

logger = MyLogger()

def read_data_from_file(file_path: str):
    if not os.path.exists(file_path):
        logger.error(f"File not found: {file_path}", exc_info=True)
        return None

    try:
        with open(file_path, 'r') as file:
            data = file.readlines()
        logger.info(f"Successfully read data from {file_path}")
    except Exception as e:
        logger.error(f"An error occurred while reading data from {file_path}", exc_info=True)
        return None

    return data

def calculate_average(numbers):
    try:
        average = sum(numbers) / len(numbers)
        logger.info(f"Calculated average: {average}")
        return average
    except ZeroDivisionError as e:
        logger.error(f"An error occurred while calculating the average", exc_info=True)
        return None
    except Exception as e:
        logger.error(f"An unexpected error occurred while calculating the average", exc_info=True)
        return None

def main():
    logger.info("Starting the application...")

    file_path = "data.txt"
    data = read_data_from_file(file_path)

    if data is not None:
        try:
            numbers = [float(x.strip()) for x in data]
        except ValueError as e:
            logger.critical("Failed to convert data to numbers. Terminating the application...", exc_info=True)
            return

        average = calculate_average(numbers)
        if average is not None:
            logger.info(f"The average of the numbers is {average}")

    logger.info("Ending the application...")

if __name__ == "__main__":
    main()
```

In this example, the application reads data from a file, converts the data into a list of numbers, and calculates the average of those numbers. The `logEZ` library is used to log messages at different logging levels, including info, error, and critical messages. The `exc_info` parameter is used to include complete execution information when logging error and critical messages.

When run, the output will look something like this (assuming the file `data.txt` does not exist):

```bash
01-04-23 15:45:36 - root : INFO : Starting the application...
01-04-23 15:45:36 - root : ERROR : File not found: data.txt
Traceback (most recent call last):
  File "example.py", line 6, in read_data_from_file
    if not os.path.exists(file_path):
FileNotFoundError: [Errno 2] No such file or directory: 'data.txt'
01-04-23 15:45:36 - root : INFO : Ending the application...
```

This output shows various log messages, including info and error messages, and includes the traceback for the `FileNotFoundError` exception because the `exc_info` parameter was set to `True`.