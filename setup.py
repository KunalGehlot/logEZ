from setuptools import setup, find_packages

classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Operating System :: OS Independent",
]

setup(
    name="log-ez",
    version="0.0.3",
    description="A simple logger for Python",
    long_description=open("README.md").read() + "\n\n" + open("CHANGELOG.txt").read(),
    url="https://github.com/KunalGehlot/log-ez",
    author="Zackcodes.ai",
    author_email="gehlotkunal@outlook.com",
    license="MIT",
    classifiers=classifiers,
    keywords="logging",
    packages=find_packages(),
    install_requires=["logging"],
)
