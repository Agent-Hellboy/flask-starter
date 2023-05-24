import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name="flask-starter",
    version="0.7.0",
    author="Prince Roshan",
    author_email="princekrroshan01@gmail.com",
    url="https://github.com/princekrroshan01/flask-starter",
    description=(
        "A flask extension which contains a basic app and is configured in your local machine through a command line utility "
    ),
    long_description=read("README.rst"),
    license="MIT",
    py_modules=["script"],
    entry_points={"console_scripts": ["flask-starter-project = script:main"]},
    install_requires=["flask", "requests", "httplib2", "click"],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    include_package_data=True,
)
