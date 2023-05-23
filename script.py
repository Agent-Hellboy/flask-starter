import os
import shutil

import click


@click.command()
@click.option("--name", help="Project name")
def main(name):
    os.system("git init")
    os.system("git clone https://github.com/princekrroshan01/flask-starter.git")
    os.remove(f"{name}/script.py")
    os.remove(f"{name}/setup.py")
    os.remove(f"{name}/LICENSE")
    os.remove(f"{name}/.gitignore")
    os.remove(f"{name}/README.rst")
    os.remove(f"{name}/requirements.txt")
    shutil.rmtree(f"{name}/.github")


if __name__ == "__main__":
    main()
