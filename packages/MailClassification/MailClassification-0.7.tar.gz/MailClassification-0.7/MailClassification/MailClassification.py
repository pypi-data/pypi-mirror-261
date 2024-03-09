from .LoadClassModel import LoadClassModel
from .LoadEmbeddsModel import LoadEmbeddsModel
from .TextCleaner import TextCleaner
from .LoadScalerModel import LoadScalerModel
import torch
import numpy as np
from joblib import dump, load
import logging


logging.basicConfig(level=logging.INFO) 

class MailClassification:
    def __init__(self):
        self.classification_model = LoadClassModel.get_model_instance()
        self.embedding_model = LoadEmbeddsModel.get_model_instance()
        self.scaler_model = LoadScalerModel.get_model_instance()
        self.text_cleaner = TextCleaner()

    def predict(self, text):
        text = self.text_cleaner.decode_into_text(text) 
        cleaned_text = self.text_cleaner.clean(text)
        result  = None
        try:
            with torch.no_grad():
                embeddings = self.embedding_model.encode(cleaned_text)
                scaled = self.scaler_model.transform(embeddings.reshape(1,-1))
                predictions = self.classification_model.predict(scaled,verbose = 0)
                result =  np.argmax(predictions)
                if result == 0:
                    return "Tonnage"
                elif result == 2:
                    return "Other"
                else:
                    return "Cargo"
        except Exception as e:
            logging.error("Error in predicting %s" , e)
        return result