import os
from shutil import rmtree
import click

@click.command()
def main():
	os.system('git init')
	os.system('git clone https://github.com/princekrroshan01/flask-starter.git')
	os.remove('README.md')
	os.remove('script.py')
	os.remove('setup.py')

	
	
