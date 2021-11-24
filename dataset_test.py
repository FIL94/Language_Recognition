from MyDataset import MyDataset

dataset = MyDataset(r'Спектры\train.csv', r'Спектры\Все')
print(dataset[0])