import os
import logging
import zipfile
import requests
from joblib import dump, load

logging.basicConfig(level=logging.INFO) 

class LoadScalerModel:
    Scaler_Model_Url = "https://d2olrrfwjazc7n.cloudfront.net/website/assets/entity_extraction_model/classification/scaler.joblib"
    BASE_DIR = os.getcwd()
    modelInstance = None

    @classmethod
    def get_model_instance(cls):
        if cls.modelInstance is None:
            cls.modelInstance = cls.load_model()
        return cls.modelInstance
    
    @classmethod
    def load_model(cls):
        try:
            logging.info("Checking Standard Scaler Model File")
            model_path = os.path.join(cls.BASE_DIR, 'scaler.joblib')
            if os.path.exists(model_path):
                logging.info("Loading Pretrained Standard Scaler Model")
                model = load(model_path)
                logging.info("Standard Scaler Model has been loaded")
                return model
            else:
                logging.info("Downloading Standard Scaler Model File")
                response = requests.get(cls.Scaler_Model_Url)
                if response.status_code == 200:
                    with open(model_path, 'wb') as f:
                        f.write(response.content)
                    logging.info("Standard Scaler Model has been downloaded")
                    model = load(model_path)
                    logging.info("Standard Scaler Model has been loaded")
                    return model
                else:
                    logging.error("Failed to download the Standard Scaler file")
                    return None
        except Exception as e:
            logging.error("Error in loading Standard Scaler file %s", e)
            return None
