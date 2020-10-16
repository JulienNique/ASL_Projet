# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 19:31:26 2020

@author: julien
"""
import random
from Node import *
from GenerationArbre import *
from RFDivisionAttribut import *

def RandomForest(Noeud, seuil, n, p):
    #n est le nombre d'arbres, p est le nombre de variables choisies aléatoirement
    forest = []
    for k in range(0,n):
        nrow = (Noeud.data).shape[0]
        rows = random.choices(range(0,nrow), k = nrow)
        dataBS = Noeud.data.iloc[rows,:]
        
        racine = Node(dataBS)
        arbre = RFGenerationArbre(racine, seuil, p)
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

