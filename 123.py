from pydub import AudioSegment
import os
import shutil
from tqdm import tqdm

init_path = r'Выборки/MP3/Немецкий язык'
dest_path = r'Выборки/WAV/Немецкий язык'
filesList = os.listdir(init_path)

for name in tqdm(filesList):
    signal = AudioSegment.from_mp3(f'{init_path}\\{name}')
    signal.export(f'{dest_path}\\{name[:-4]}.wav', format='wav')
