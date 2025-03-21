import os
import yaml
from src.mydatascienceproject import logger
import json 
import joblib
from ensure import ensure_annotations  #enforce datatype strictness 
from box import ConfigBox
from pathlib import Path
from typing import Any
from  box.exceptions import BoxValueError
import pandas as pd

@ensure_annotations
def read_yaml(path_to_yaml: Path ) -> ConfigBox:
    """
    read_yaml file

    Args:
        path_to_yaml (Path): original yaml file path 
        
    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox Type
    """
    try: 
        with open(path_to_yaml) as yf:
            content = yaml.safe_load(yf)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e
    
    
    @ensure_annotations
    def create_directories(path_to_directories: list, verbose = True):
        """
        create_directories creates directories for each filepath in a list
        Args:
            path_to_directories (list): list of filepaths
            verbose (bool, optional): ignore if multiple dirs specified. Defaults to True.
        """
        
        for path in path_to_directories:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f"created directory at:{path}")
                
    @ensure_annotations
    def save_json(path: Path, data: dict):
        """
        save_json saves given data to the Path as json file.

        Args:
            path (Path): path to save the json file
            data (dict): data to save
        """
        pd.to_json(path, data)
        logger.info(f"json file saved at: {path}")
        
    @ensure_annotations
    def load_json(path: Path):
        """
        load_json loads given json file.

        Args:
            path (Path): path to save the json file
            data (dict): data to save
        """
        content = pd.read_json(path)
        logger.info(f"json file loaded from: {path}")
        return ConfigBox(content)
    
    @ensure_annotations
    def save_bin(data: Any, path: Path):
        """
        save_bin save binary file

        Args:
            data (Any): data to be saved as binary
            path (Path): path to save binary file
        """
        joblib.dump(value=data, filename=path)
        logger.info(f"Binary file saved at:{path}")
        
        
    @ensure_annotations
    def load_bin(path: Path) -> Any:
        """
        load_bin loads binary file

        Args:
            path (Path): Path to load from

        Returns:
            Any: object stored in the file
        """
        
        data = joblib.load(path)
        logger.info(f"Binary file loaded from: {path}")
        return data