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
    f"src/{project_name}/utils/common.py",
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
    "research/01_data_ingestion.ipynb",
    "research/02_prepare_base_model.ipynb",
    "research/03_model_training.ipynb",
    "research/04_model_evaluation.ipynb",
    "main.py",
    "app.py",
    "Dockerfile",
    ".gitignore",
    "templates/index.html",   # For Flask/FastAPI UI
    "test.py",
]

for filepath in list_of_files:
    filepath_obj = Path(filepath)

    # Create directory if it doesn't exist (handles root directory '.' safely)
    filepath_obj.parent.mkdir(parents=True, exist_ok=True)

    try:
        # Create empty file if it doesn't exist or is currently 0 bytes
        if not filepath_obj.exists() or filepath_obj.stat().st_size == 0:
            filepath_obj.touch()
            logging.info(f"Created/verified empty file: {filepath_obj}")
        else:
            logging.info(f"File already exists and is not empty: {filepath_obj}")
    except Exception as e:
        logging.error(f"Error handling file {filepath_obj}: {e}")