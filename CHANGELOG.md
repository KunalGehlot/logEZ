# Change Log

## Unreleased

## [0.1.0]
### Updated
- Refactored the code to adhere to PEP8 standards for better readability and maintainability.
- Added type hints to function signatures for improved code comprehension and editor support.
- Improved exception handling with more specific exceptions and error messages.
- Modularized the code into separate files for better organization and extensibility:
  - `mylogger.py`: Contains the main `MyLogger` class.
  - `handlers.py`: Contains handlers for logging to files and consoles.
  - `formatters.py`: Contains the log formatter used for log messages.
- Updated the `__init__.py` file to import necessary components for easier library usage.
- Enhanced the library with docstrings for better documentation and understanding.
- Updated the `README.md` file to provide clearer instructions on how to use the library, including examples and explanations of the new features.
- Improved the `setup.py` file to adhere to the latest Python norms and standards.
- Added `nox` as a development dependency to simplify the development workflow.

## [0.0.3] - 2022-05-08
### Updated
- Updated code with method name fix and logging level method.
- Added "How to use" with complete method definition in README.md

## [0.0.2] - 2022-05-08
### Fixed
- Fixing project directory name

## [0.0.1] - 2022-05-08
### Added
- First Release
### Removed
- Removed `requirements.txt`
- Removed `logging` from `install_requires`