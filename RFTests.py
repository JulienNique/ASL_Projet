# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 08:49:51 2020

@author: julien
"""
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris 
from RandomForest import *

#iris = load_iris()
#target = (iris.target).reshape(len(iris.target),1)
#data = pd.DataFrame(np.concatenate((iris.data, target), axis = 1),
#                    columns = ['sepl', 'sepw', 'petl', 'petw', 'spec'])

#Titanic
data = pd.read_csv("C:/Users/julien/Google Drive/DataSience/Machine Learning/Titanic/all/train.csv", sep=";")
data.dropna(subset=['Age'], how='all', inplace = True)

data = data[['Age','Pclass','Sex', 'Survived']]
data_train, data_test = train_test_split(data, test_size=0.20)

noeud = Node(data_train)
forest = RandomForest(noeud, 1, 10, 3)

#x = data.iloc[range(60,71),:]
ypred = RFPrediction(forest, data_test)
score = sum(ypred == data_test['Survived'])/len(ypred)
print('Le score est de :', score)