import os
import platform
import shutil
import subprocess
import sys

import click


def ready():

    # Create a virtual environment
    venv_dir = '.venv'
    python_executable = sys.executable
    subprocess.run([python_executable, '-m', 'venv', venv_dir])

    current_os = platform.system()
    if current_os == 'Windows':
        activate_script = os.path.join(venv_dir, 'Scripts', 'activate')
    elif current_os == 'Linux' or current_os == 'Darwin':  # Unix/Linux/MacOS
        activate_script = os.path.join(venv_dir, 'bin', 'activate')
    else:
        raise OSError(f"Unsupported operating system: {current_os}")
    subprocess.run(activate_script, shell=True)

    # Install dependencies from requirements.txt
    requirements_file = 'requirements.txt'
    subprocess.run([python_executable, '-m', 'pip', 'install', '-r', requirements_file])

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
    ready()


if __name__ == "__main__":
    main()
