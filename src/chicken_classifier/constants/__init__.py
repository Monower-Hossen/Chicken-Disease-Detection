import os
from pathlib import Path

# Get the absolute path of the current file
CURRENT_FILE_PATH = Path(__file__).resolve()

# Navigate up to the project root directory
PROJECT_ROOT = CURRENT_FILE_PATH.parents[3] # src/chicken_classifier/constants/__init__.py -> src/chicken_classifier/constants -> src/chicken_classifier -> src -> Chicken-Disease-Detection (project root)

CONFIG_FILE_PATH = Path(os.path.join(PROJECT_ROOT, "config", "config.yaml"))
PARAMS_FILE_PATH = Path(os.path.join(PROJECT_ROOT, "params.yaml"))