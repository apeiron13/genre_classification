from tensorflow import keras
import numpy as np

PATH_MODEL_H5 = './model_nn/music_genre_classification.h5'


class Genre:
    def __init__(self):
        self.model = keras.models.load_model(PATH_MODEL_H5)

    def genre_number(self, i):
        if i == 0:
            return 'Hip-Hop'
        elif i == 1:
            return 'Pop'
        elif i == 2:
            return 'Folk'
        elif i == 3:
            return 'Rock'
        elif i == 4:
            return 'Experimental'
        elif i == 5:
            return 'International'
        elif i == 6:
            return 'Electronic'
        else:
            return 'Instrumental'

    def reshape_in_data(self, data):
        return np.array([x.reshape((128, 431, 1)) for x in data])

    def predict_classes(self, data):
        result = self.model.predict_classes(self.reshape_in_data(data))
        return [self.genre_number(item) for item in result]
