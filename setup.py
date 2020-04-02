import os
from setuptools import setup, find_packages

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="flask-starter",
    version="0.1",
    author="Prince Roshan",
    author_email="princekrroshan01@gmail.com",
    url="https://github.com/princekrroshan01/flask-starter",
    description=(""),
    long_description=read('README.md'),
    license="MIT",
    py_modules=['script'],
    entry_points={'console_scripts': ['flask-starter-project = script:main']},
    install_requires=['flask','requests','httplib2','click','shutil'],
    include_package_data=True
)

