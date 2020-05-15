import matplotlib.pyplot as plt
import librosa
import librosa.display
import numpy as np
import os
from pydub import AudioSegment
from pathlib import Path

from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas


class Music(object):
    def __init__(self, key, file_path):
        self.key = str(key)
        self.files_path = file_path
        self.melspectrogram = []
        self.list_img_path = []
        self.names = []

    def set_melspectrogram(self):
        # no convert wav to mp3
        for file in os.listdir(self.files_path):
            if str(file)[:len(self.key)] == self.key:
                y, sr = librosa.load(self.files_path + file, duration=10)
                ps = librosa.feature.melspectrogram(y=y, sr=sr, n_mels=128)
                self.melspectrogram.append(ps)
                self.names.append(file[:-4])
                os.remove(self.files_path + file)

    def save_melspgram_by_genre(self, genre):
        for mel, g, name in zip(self.melspectrogram, genre, self.names):
            fig = plt.Figure()
            canvas = FigureCanvas(fig)
            ax = fig.add_subplot(111)
            p = librosa.display.specshow(librosa.power_to_db(mel, ref=np.max), ax=ax, y_axis='mel', x_axis='time')
            plt.title('Mel spectrogram')
            plt.tight_layout()
            fig.savefig(self.files_path + name + '_' + g + '.png')
            self.list_img_path.append(name + '_' + g + '.png')

    def get_melspectrogram(self):
        return self.melspectrogram

    def get_list_img_path(self):
        return self.list_img_path

    def get_names(self):
        return [item[len(self.key) + 1:] for item in self.names]