import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="flask-starter",
    version="0.2",
    author="Prince Roshan",
    author_email="princekrroshan01@gmail.com",
    url="https://github.com/princekrroshan01/flask-starter",
    description=("A flask extension which contains a basic app and is configured in your local machine through a command line utility "),
    long_description=read('README.md'),
    license="MIT",
    py_modules=['script'],
    entry_points={'console_scripts': ['flask-starter-project = script:main']},
    install_requires=['flask','requests','httplib2','click'],
    include_package_data=True
)

