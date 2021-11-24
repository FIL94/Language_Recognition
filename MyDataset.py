import numpy as np
import pandas as pd
import os
from torch.utils.data import Dataset


class MyDataset(Dataset):
    def __init__(self, annotations_file, spec_dir, transform=None, target_transform=None):
        self.spec_labels = pd.read_csv(annotations_file)
        self.spec_dir = spec_dir
        self.transform = transform
        self.target_transform = target_transform

    def __len__(self):
        return len(self.spec_labels)

    def __getitem__(self, idx):
        spec_path = os.path.join(self.spec_dir, self.spec_labels.iloc[idx, 1])
        spec = np.load(spec_path)
        label = self.spec_labels.iloc[idx, 2]
        if self.transform:
            spec = self.transform(spec)
        if self.target_transform:
            label = self.target_transform(label)
        return spec, label
