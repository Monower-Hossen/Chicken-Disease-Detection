import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import os

class PredictionPipeline:
    def __init__(self, filename):
        self.filename = filename
        # Load the final trained model once during initialization to improve prediction speed
        self.model = load_model(os.path.join("artifacts", "training", "model.keras"))

    def predict(self):
        # Preprocess the incoming image
        test_image = image.load_img(self.filename, target_size=(224, 224))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis=0)
        test_image = test_image / 255.0  # Normalize as we did in training

        # Get prediction
        result = np.argmax(self.model.predict(test_image), axis=1)
        prediction_index = result[0]

        if prediction_index == 1:
            prediction = 'Healthy'
        elif prediction_index == 0:
            prediction = 'Coccidiosis'
        elif prediction_index == 2:
            prediction = 'New Castle Disease'
        else:
            prediction = 'Salmonella'

        return [{"image": prediction}]