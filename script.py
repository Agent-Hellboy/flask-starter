import os
import shutil

import click


def move(source_directory,destination_directory):
    items = os.listdir(source_directory)
    
    # Move each item to the destination directory
    for item in items:
        source_path = os.path.join(source_directory, item)
        destination_path = os.path.join(destination_directory, item)
        shutil.move(source_path, destination_path)

@click.command()
@click.option("--name", help="Project name")
def main(name):
    os.system("git init")
    os.system("git clone https://github.com/princekrroshan01/flask-starter.git")
    os.mkdir(name)
    move("flask-starter",name)
    os.remove(f"{name}/script.py")
    os.remove(f"{name}/setup.py")
    os.remove(f"{name}/LICENSE")
    os.remove(f"{name}/.gitignore")
    os.remove(f"{name}/README.rst")
    shutil.rmtree(f"{name}/.github")
    shutil.rmtree("flask-starter")
    shutil.rmtree(f"{name}/.git")


if __name__ == "__main__":
    main()
