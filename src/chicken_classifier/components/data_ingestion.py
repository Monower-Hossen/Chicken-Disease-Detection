import os
import urllib.request as request
import zipfile
from pathlib import Path
from chicken_classifier import logger
from chicken_classifier.utils.common import get_size
from chicken_classifier.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        """
        Downloads the file from the source URL.
        """
        if not os.path.exists(self.config.local_data_file):
            logger.info(f"Downloading from {self.config.source_URL}...")
            
            # Some servers block requests without a proper User-Agent. 
            # Installing a global opener with a browser-like header.
            opener = request.build_opener()
            opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)')]
            request.install_opener(opener)

            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )
            logger.info(f"{filename} download! with following info: \n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)