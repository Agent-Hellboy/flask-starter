import logging
import os
import shutil
import site
from pathlib import Path
from typing import Optional

import click
from rich.console import Console
from rich.logging import RichHandler

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(rich_tracebacks=True)]
)
logger = logging.getLogger("flask-starter")

# Initialize Rich console for better output
console = Console()

# Constants
PACKAGE_NAME = "flask-starter"
FILES_TO_REMOVE = [
    "script.py",
    "setup.py",
    "LICENSE",
    ".gitignore",
    "README.rst"
]
DIRS_TO_REMOVE = [
    ".github",
    ".git"
]

class FlaskStarterError(Exception):
    """Base exception for Flask Starter errors."""
    pass

class ProjectCreationError(FlaskStarterError):
    """Exception raised when project creation fails."""
    pass

def setup_logging(verbose: bool) -> None:
    """Configure logging level based on verbosity."""
    level = logging.DEBUG if verbose else logging.INFO
    logger.setLevel(level)

def validate_project_name(name: str) -> None:
    """Validate the project name."""
    if not name:
        raise click.BadParameter("Project name cannot be empty")
    
    if not name.isalnum() and not all(c.isalnum() or c in '-_' for c in name):
        raise click.BadParameter("Project name can only contain alphanumeric characters, hyphens, and underscores")
    
    if os.path.exists(name):
        raise click.BadParameter(f"Directory '{name}' already exists")

def get_package_path() -> Path:
    """Get the path to the installed package."""
    try:
        # First try to import the package
        import flask_starter
        package_path = Path(flask_starter.__file__).parent
        if package_path.exists():
            return package_path
    except ImportError:
        pass

    # Try to find the package in site-packages
    for site_dir in site.getsitepackages():
        # Check for both regular and editable installs
        possible_paths = [
            Path(site_dir) / PACKAGE_NAME,
            Path(site_dir) / f"{PACKAGE_NAME}.egg-link",
            Path(site_dir) / f"{PACKAGE_NAME}-*.egg-link"
        ]
        
        for path in possible_paths:
            if path.exists():
                if path.suffix == '.egg-link':
                    # For editable installs, read the link file
                    with open(path) as f:
                        linked_path = Path(f.read().strip())
                        if linked_path.exists():
                            return linked_path
                else:
                    return path

    # If we're in the development directory, use that
    current_dir = Path.cwd()
    if (current_dir / "app").exists() and (current_dir / "server.py").exists():
        return current_dir

    raise ProjectCreationError(f"Could not find {PACKAGE_NAME} package. Please install it first.")

def move_files(source_dir: Path, dest_dir: Path) -> None:
    """Move files from source directory to destination directory."""
    try:
        # List of files and directories to copy
        COPY_LIST = [
            "app",
            "requirements.txt",
            "server.py",
        ]
        
        for item_name in COPY_LIST:
            source_path = source_dir / item_name
            dest_path = dest_dir / item_name
            
            if not source_path.exists():
                logger.warning(f"Source path {source_path} does not exist, skipping...")
                continue
                
            if source_path.is_dir():
                if dest_path.exists():
                    shutil.rmtree(dest_path)
                shutil.copytree(str(source_path), str(dest_path))
                logger.debug(f"Copied directory: {item_name}")
            else:
                shutil.copy2(str(source_path), str(dest_path))
                logger.debug(f"Copied file: {item_name}")
                
    except (shutil.Error, OSError) as e:
        raise ProjectCreationError(f"Failed to copy files: {str(e)}")

def create_project(name: str, verbose: bool) -> None:
    """Create a new Flask project."""
    setup_logging(verbose)
    
    try:
        # Validate project name
        validate_project_name(name)
        
        with console.status("[bold green]Creating Flask project...") as status:
            # Get package path
            package_path = get_package_path()
            logger.debug(f"Using package from: {package_path}")
            
            # Create project directory
            project_dir = Path(name)
            project_dir.mkdir(exist_ok=True)
            
            # Copy files from package to project directory
            logger.info("Copying project files...")
            move_files(package_path, project_dir)
            
            # Initialize git repository
            logger.info("Initializing git repository...")
            os.system(f"cd {name} && git init")
            
            logger.info(f"Successfully created Flask project: {name}")
            console.print(f"\n[bold green]Project '{name}' created successfully![/bold green]")
            console.print("\nProject Structure:")
            console.print("├── app/")
            console.print("│   ├── __init__.py          # App initialization")
            console.print("│   ├── models.py            # Database models")
            console.print("│   ├── views.py             # Route handlers")
            console.print("│   ├── extension.py         # Flask extensions")
            console.print("│   ├── libs/                # Add your libraries here")
            console.print("│   └── templates/           # Jinja2 templates")
            console.print("├── tests/                   # Add your tests here")
            console.print("├── requirements.txt         # Dependencies")
            console.print("└── server.py               # Entry point")
            
            console.print("\n[bold yellow]Development Guidelines:[/bold yellow]")
            console.print("1. Add your business logic in [bold]app/libs/[/bold]")
            console.print("2. Create new views as blueprints in [bold]app/views.py[/bold]")
            console.print("3. Write tests in [bold]tests/[/bold] directory")
            console.print("4. Add new dependencies to [bold]requirements.txt[/bold]")
            
            console.print("\n[bold blue]Next steps:[/bold blue]")
            console.print("1. cd " + name)
            console.print("2. python -m venv venv")
            console.print("3. source venv/bin/activate  # On Windows: venv\\Scripts\\activate")
            console.print("4. pip install -r requirements.txt")
            console.print("5. python server.py")
            
    except ProjectCreationError as e:
        logger.error(f"Failed to create project: {str(e)}")
        raise click.Abort()
    except Exception as e:
        logger.error(f"An unexpected error occurred: {str(e)}")
        raise click.Abort()

@click.command()
@click.option(
    "--name",
    prompt="Project name",
    help="Name of the Flask project to create"
)
@click.option(
    "--verbose",
    "-v",
    is_flag=True,
    help="Enable verbose output"
)
def main(name: str, verbose: bool) -> None:
    """Create a new Flask project with a basic structure and authentication."""
    create_project(name, verbose)

if __name__ == "__main__":
    main()
