from cnnClassifier.entity import TrainingConfig
import tensorflow as tf
from pathlib import Path

class Training:
    def __init__(self, config: TrainingConfig):
        self.config = config

    
    def get_base_model(self):
        self.model = tf.keras.models.load_model(
            self.config.updated_base_model_path
        )
    def train_valid_generator(self): 
         datagenerator_kwargs = dict(
                                  rescale = 1./255,
                                  shear_range = 0.2,
                                  zoom_range = 0.2,
                                  horizontal_flip = True)
         train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
            )   
         testgenerator_kwargs = dict(rescale = 1./255)
         test_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **testgenerator_kwargs
            )
         self.train_generator = train_datagenerator.flow_from_directory(directory = self.config.training_data,
                                                 target_size = (224, 224),
                                                 batch_size = 32,
                                                 class_mode = 'categorical')
         self.test_generator = test_datagenerator.flow_from_directory(directory = self.config.testing_data,
                                                 target_size = (224, 224),
                                                 batch_size = 32,
                                                 class_mode = 'categorical')
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)

    def train(self,callback_list: list,):
        self.model.fit(
            self.train_generator,
            validation_data=self.test_generator,
            epochs=self.config.params_epochs,
            steps_per_epoch=len(self.train_generator),
            validation_steps=len(self.test_generator),
            callbacks=callback_list
        )
        self.save_model(
            path=self.config.trained_model_path,
            model=self.model
        )
        
         

    
    