import pandas as pd
import numpy as np

train = pd.read_csv('datas/train.csv')
test = pd.read_csv('datas/test.csv')

print(test['Embarked'].value_counts())