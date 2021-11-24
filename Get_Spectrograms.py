import numpy as np
import librosa
from tqdm import tqdm
import os

block_size = 1024
overlap = 0.5

init_path = r'Выборки/WAV/Русский язык'
dest_path = r'Спектры/Русский язык'
filesList = os.listdir(init_path)

for name in tqdm(filesList):
    signal, Fs = librosa.load(f'{init_path}\\{name}', librosa.get_samplerate(f'{init_path}\\{name}'))
    signal_spec = librosa.stft(signal, block_size, int(block_size * overlap), block_size, 'hamming', False)
    signal_spec = np.abs(signal_spec) ** 2
    np.save(f'{dest_path}\\{name[:-4]}.npy', signal_spec)

