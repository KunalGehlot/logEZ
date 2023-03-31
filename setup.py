from setuptools import setup, find_packages

classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Operating System :: OS Independent",
]

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("CHANGELOG.md", "r", encoding="utf-8") as fh:
    long_description += "\n\n" + fh.read()

setup(
    name="logEZ",
    version="0.1.0",
    description="A simple(r) logger for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KunalGehlot/logEZ",
    author="Zackcodes.ai",
    author_email="gehlotkunal@outlook.com",
    license="MIT",
    classifiers=classifiers,
    keywords="logging",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[],
)
