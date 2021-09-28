import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier

train = pd.read_csv('datas/train.csv')
test = pd.read_csv('datas/test.csv')

modelo = RandomForestClassifier(n_estimators=100, n_jobs=-1, random_state=0)

def transformar_sexo(valor):
    if valor == 'female':
        return 1
    else:
        return 0

train['Sex_bin'] = train['Sex'].map(transformar_sexo)

variaveis = ['Sex_bin', 'Age']

X = train[variaveis]
Y = train['Survived']

print(X)
print(Y)

