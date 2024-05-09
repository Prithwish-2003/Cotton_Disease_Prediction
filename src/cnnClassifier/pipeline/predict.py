import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

class CottonDisease:
    def __init__(self,filename):
        path = os.path.join("uploads",filename)
        self.filename = path

    def model_predict(self):
        model = load_model(os.path.join("artifacts","training", "model.h5"))
        imagename = self.filename
        print(imagename)
        img = image.load_img(imagename, target_size=(224, 224))

        # Preprocessing the image
        x = image.img_to_array(img)
        # x = np.true_divide(x, 255)
        ## Scaling
        x=x/255
        x = np.expand_dims(x, axis=0)
    

        # Be careful how your trained model deals with the input
        # otherwise, it won't make correct prediction!
    # x = preprocess_input(x)

        preds = model.predict(x)
        preds=np.argmax(preds, axis=1)
        if preds==0:
            preds="The leaf is diseased cotton leaf"
            return preds
        elif preds==1:
            preds="The leaf is diseased cotton plant"
            return preds
        elif preds==2:
            preds="The leaf is fresh cotton leaf"
            return  preds
        else:
            preds="The leaf is fresh cotton plant"
            return  preds