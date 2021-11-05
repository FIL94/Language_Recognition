import os
import librosa
import pydub
from tqdm import tqdm
from pydub import AudioSegment

init_path = r"C:\Users\admin\Desktop\Python Projects\Language Recognition\Выборки\Французский язык"
dest_path = r"C:\Users\admin\Desktop\Python Projects\Language Recognition\Спектры\Французский язык"

# for f in tqdm(os.listdir(init_path)):
#     signal, Fs = AudioSegment.from_mp3(f"{init_path}\{f}")
#
# print(type(signal))
signal = AudioSegment.from_mp3(r"Выборки/Французский язык/common_voice_fr_17319928.mp3")
