from cnnClassifier.config import ConfigurationManager
from cnnClassifier.components.prepare_base_model import PrepareBaseModel    
from cnnClassifier import logger

class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        Prepare_base_model_config = config.get_prepare_base_model_config()
        Prepare_base_model = PrepareBaseModel(config=Prepare_base_model_config)
        Prepare_base_model.get_base_model()
        Prepare_base_model.update_base_model()