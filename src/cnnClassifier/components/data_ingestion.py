import os
import urllib.request as request
from zipfile import ZipFile
from tqdm import tqdm
from pathlib import Path
from cnnClassifier.entity import DataIngestionConfig
from cnnClassifier import logger
from cnnClassifier.utils import get_size


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def _get_updated_list_of_files(self,list_of_files):
        list = []
        for i in list_of_files:
                dir , file = os.path.split(i)
                if "test data comp files" not in dir :
                        list.append(i)
                else :
                        continue
                
        return list
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with ZipFile(self.config.local_data_file, 'r') as zip_ref:
            list = zip_ref.namelist()
            list =self._get_updated_list_of_files(list)
            for i in list :
                target_filepath = os.path.join(unzip_path, i)
                if not os.path.exists(target_filepath):  
                        zip_ref.extract(i,unzip_path)
