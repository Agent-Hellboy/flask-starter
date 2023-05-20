import os
import shutil

import click

"""
#process_with_auth
need to copy extra files in templates and static  
#process_without_auth 
"""


@click.command()
def main():
    os.system("git init")
    os.system("git clone https://github.com/princekrroshan01/flask-starter.git")
    os.remove("flask-starter/script.py")
    os.remove("flask-starter/setup.py")
    os.remove("flask-starter/LICENSE")
    os.remove("flask-starter/.gitignore")
    os.remove("flask-starter/README.rst")
    os.remove("flask-starter/requirements.txt")
    shutil.rmtree('.github')


if __name__ == "__main__":
    main()
