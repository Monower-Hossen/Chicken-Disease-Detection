import os
import sys
import logging

# Suppress oneDNN custom operations warning and improve TensorFlow initialization stability
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Create logs directory if it doesn't exist
log_dir = "logs"
log_filepath = os.path.join(log_dir, "running_logs.log")
os.makedirs(log_dir, exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format=logging_str,
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

# Define the logger
logger = logging.getLogger("chickenClassifierLogger")