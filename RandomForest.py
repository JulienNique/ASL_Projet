# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 19:31:26 2020

@author: julien
"""
import random
from DivisionAttribut import *
from Node import *
from sklearn.model_selection import train_test_split
from collections import Counter


def RandomForest(Noeud, n):
    forest = []
    for k in range(0,n):
        nrow = (Noeud.data).shape[0]
        rows = random.choices(range(0,nrow), k = nrow)
        dataBS = Noeud.data.iloc[rows,:]
        
        racine = Node(dataBS)
        arbre = GenerationArbre(racine)
        forest.append(arbre)
    return forest

def RFPrediction(forest, x):
    y = []
    for arbre in forest:
        y.append(Prediction(arbre,x))
        A = np.transpose(np.matrix(y))
        ypreds = []
        for k in range(0,A.shape[0]):
            row = A[k,:].tolist()[0]
            ypreds.append(max(row, key=row.count))
    
    return ypreds


from sklearn.datasets import load_iris 
iris = load_iris()
target = (iris.target).reshape(len(iris.target),1)
data = pd.DataFrame(np.concatenate((iris.data, target), axis = 1),
                    columns = ['sepl', 'sepw', 'petl', 'petw', 'spec'])

data_train, data_test = train_test_split(data, test_size=0.30)

noeud = Node(data_train)
forest = RandomForest(noeud,5)

#x = data.iloc[range(60,71),:]
ypred = RFPrediction(forest, data_test)
score = sum(ypred == data_test['spec'])/len(ypred)
print('Le score est de :', score)