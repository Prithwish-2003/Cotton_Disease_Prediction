import tensorflow as tf
from pathlib import Path
from cnnClassifier.entity import EvaluationConfig
from cnnClassifier.utils import save_json

class Evaluation:
    def __init__(self, config: EvaluationConfig):
        self.config = config

    
    def _evaluation_generator(self):

        testgenerator_kwargs = dict(rescale = 1./255)
        test_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **testgenerator_kwargs
            )
        self.test_generator = test_datagenerator.flow_from_directory(directory = self.config.testing_data,
                                                 target_size = self.config.params_image_size[:-1],
                                                 batch_size = self.config.params_batch_size,
                                                 class_mode = 'categorical')

    
    @staticmethod
    def load_model(path: Path) -> tf.keras.Model:
        return tf.keras.models.load_model(path)
    

    def evaluation(self):
        self.model = self.load_model(Path(self.config.path_of_model))
        self._evaluation_generator()
        self.score = self.model.evaluate(self.test_generator)

    
    def save_score(self):
        scores = {"loss": self.score[0], "accuracy": self.score[1]}
        save_json(path=Path("scores.json"), data=scores)
