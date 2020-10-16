# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 08:49:51 2020

@author: julien
"""

from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris 
from RandomForest import *

iris = load_iris()
target = (iris.target).reshape(len(iris.target),1)
data = pd.DataFrame(np.concatenate((iris.data, target), axis = 1),
                    columns = ['sepl', 'sepw', 'petl', 'petw', 'spec'])

data_train, data_test = train_test_split(data, test_size=0.30)

noeud = Node(data_train)
forest = RandomForest(noeud, 0, 5, 3)

#x = data.iloc[range(60,71),:]
ypred = RFPrediction(forest, data_test)
score = sum(ypred == data_test['spec'])/len(ypred)
print('Le score est de :', score)