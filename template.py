import os
from pathlib import Path
import logging

# Logging configuration to track file creation
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

project_name = "chicken_classifier"

list_of_files = [
    ".github/workflows/.gitkeep", # For CI/CD deployment
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "dvc.yaml",      # For Data Version Control
    "params.yaml",   # For Hyperparameters
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb", # For experimentation
    "templates/index.html",   # For Flask/FastAPI UI
    "test.py"
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # Create directory if it doesn't exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    # Create empty file if it doesn't exist or is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating empty file: {filepath}")

    else:
        logging.info(f"{filename} already exists")