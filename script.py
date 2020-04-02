import os
from shutil import rmtree
import click

@click.command()
def main():
	os.system('git init')
	os.system('git clone https://github.com/princekrroshan01/flask-starter.git')
	os.remove('flask-starter/script.py')
	os.remove('flask-starter/setup.py')
	os.remove('flask-starter/LICENSE')
	os.remove('flask-starter/.gitignore')
	os.remove('flask-starter/README.md')
	os.remove('flask-starter/requiremets.txt')

	
if(__name__=='__main__'):
	main()
	
	
