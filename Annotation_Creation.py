import os
import shutil
import pandas as pd

train_ratio = 0.8

folders = os.listdir(r'Спектры')
train_df = pd.DataFrame(columns=['Name', 'Class'])
test_df = pd.DataFrame(columns=['Name', 'Class'])

for folder in folders:
    local_list = os.listdir(os.path.join(r'Спектры', folder))
    local_df = pd.DataFrame(index=range(len(local_list)), columns=['Name', 'Class'])

    for [ind, file] in enumerate(local_list):
        local_df['Name'].iloc[ind] = file
        local_df['Class'].iloc[ind] = folders.index(folder)-1
        shutil.copy(os.path.join(r'Спектры', folder, file), os.path.join(r'Спектры', r'Все'), )

    train_df = pd.concat([train_df, local_df.iloc[:int(train_ratio * len(local_list))]], ignore_index=True)
    test_df = pd.concat([test_df, local_df.iloc[int(train_ratio * len(local_list)):]], ignore_index=True)

train_df.to_csv(path_or_buf=os.path.join(r'Спектры', 'train.csv'))
test_df.to_csv(path_or_buf=os.path.join(r'Спектры', 'test.csv'))
print(train_df.shape)
