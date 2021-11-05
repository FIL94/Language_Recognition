import os
import shutil
import numpy as np
from tqdm import tqdm

init_path = r'D:\Наборы данных\Французский язык'
dest_path = r'C:\Users\admin\Desktop\Python Projects\Language Recognition\Выборки\Французский язык'
filesList = os.listdir(init_path)
idx = np.random.randint(0, len(filesList), 100, int)
if not os.path.isdir(dest_path):
    os.mkdir(dest_path)

for i in tqdm(idx):
    shutil.copy(f'{init_path}\\{filesList[i]}', f'{dest_path}\\{filesList[i]}')
