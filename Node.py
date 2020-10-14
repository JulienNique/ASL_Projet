# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 10:43:27 2020

@author: jnique
"""

from DivisionAttribut import *

class Node:

    def __init__(self, data):
        self.data = data
        self.child = []
        self.parent = None
        self.classeMaj = data.iloc[:,-1].value_counts().idxmax()
        self.var = []
        self.leaf = False

    def __str__(self):
        return str(self.data)

def ParcoursArbre(Arbre):
    print(Arbre.leaf)
    print(Arbre.var)
    print(Arbre.classeMaj)
    print('\n')
    if Arbre.child != []:
        for child in Arbre.child:
            ParcoursArbre(child)
    
def Prediction(Arbre,X):
    ypred = []
    for index, x in X.iterrows():
        noeud = Arbre
        while noeud.leaf == False:
            #print(noeud.var)
            if len(noeud.var) == 2:
                if x[noeud.var[0]] <= noeud.var[1]:
                    noeud = noeud.child[0]
                else:
                    noeud = noeud.child[1]
            else:
                pos = noeud.var[1:].index(x[noeud.var[0]])-1
                noeud = noeud.child[pos]
                
        ypred.append(noeud.classeMaj)
    return ypred


"""GenerationArbre"""
def GenerationArbre(Noeud, seuil):
    data = Noeud.data
    [attr, so, MinE] = DivisionAttribut(data)
    #print([attr, so, MinE])
    if(MinE > seuil and MinE != 10):
        Noeud.var = [attr, so]
        if  data[attr].dtypes == 'float64':
            noeud = Node(data.loc[data[attr] <= so])
            Noeud.child.append(noeud)
            noeud.parent = Noeud    
            
            noeud = Node(data.loc[data[attr] > so])
            Noeud.child.append(noeud)
            noeud.parent = Noeud
        else:
            Noeud.var.pop(1)
            if len(np.unique(data[attr])) >= 2:
                for val in data[attr].value_counts().index:
                    Noeud.var.append(val)
                    noeud = Node(data.loc[data[attr] == val])
                    Noeud.child.append(noeud)
                    noeud.parent = Noeud
                    
        for child in Noeud.child:
                GenerationArbre(child, seuil)
    else:
        Noeud.leaf = True
    
    return Noeud