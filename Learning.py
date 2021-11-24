import torch
from MyDataset import MyDataset
from torch import nn
from torch.utils.data import DataLoader
from torchvision.transforms import ToTensor

train_dataset = MyDataset(
    annotations_file='Спектры\\train.csv',
    spec_dir='Спектры\\Все')