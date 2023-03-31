import nox

# Set default Python versions for test sessions
PYTHON_VERSIONS = ["3.8", "3.9", "3.10"]

# Set locations for linting and formatting
LOCATIONS = ["logez", "tests", "noxfile.py", "setup.py"]


@nox.session
def format_apply(session):
    """
    Apply code formatting using black (modifies files in-place).
    """
    session.install("black")
    session.run("black", *LOCATIONS, "--line-length=79")


@nox.session
def lint(session):
    """
    Perform linting with flake8.
    """
    session.install("flake8")
    session.run("flake8", *LOCATIONS)


@nox.session(python=PYTHON_VERSIONS)
def tests(session):
    """
    Run test suite with pytest.
    """
    session.install("pytest")
    session.install("-r", "requirements.txt")
    session.run("pytest", "tests")
