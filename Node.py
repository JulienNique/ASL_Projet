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
        self.split = []
        self.var = data.columns.delete(-1)
        self.leaf = False

    def __str__(self):
        return str(self.data)

def ParcoursArbre(Arbre):
    print(Arbre.leaf)
    print(Arbre.split)
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
            #print(noeud.split)
            if len(noeud.split) == 2:
                if x[noeud.split[0]] <= noeud.split[1]:
                    noeud = noeud.child[0]
                else:
                    noeud = noeud.child[1]
            else:
                pos = noeud.split[1:].index(x[noeud.split[0]])-1
                noeud = noeud.child[pos]
                
        ypred.append(noeud.classeMaj)
    return ypred


"""GenerationArbre"""
def GenerationArbre(Noeud, seuil):
    data = Noeud.data
    [attr, so, MinE] = DivisionAttribut(data)
    #print([attr, so, MinE])
    if(MinE > seuil and MinE != 10):
        Noeud.split = [attr, so]
        if  data[attr].dtypes == 'float64':
            noeud = Node(data.loc[data[attr] <= so])
            Noeud.child.append(noeud)
            noeud.parent = Noeud    
            
            noeud = Node(data.loc[data[attr] > so])
            Noeud.child.append(noeud)
            noeud.parent = Noeud
        else:
            Noeud.split.pop(1)
            if len(np.unique(data[attr])) >= 2:
                for val in data[attr].value_counts().index:
                    Noeud.split.append(val)
                    noeud = Node(data.loc[data[attr] == val])
                    Noeud.child.append(noeud)
                    noeud.parent = Noeud
                    
        for child in Noeud.child:
                GenerationArbre(child, seuil)
    else:
        Noeud.leaf = True
    
    return Noeud


"""RFGenerationArbre"""
def RFGenerationArbre(Noeud, seuil):
    data = Noeud.data
    [attr, so, MinE] = RFDivisionAttribut(data)
    #print([attr, so, MinE])
    if(MinE > seuil and MinE != 10):
        Noeud.split = [attr, so]
        if  data[attr].dtypes == 'float64':
            noeud = Node(data.loc[data[attr] <= so])
            Noeud.child.append(noeud)
            noeud.parent = Noeud    
            
            noeud = Node(data.loc[data[attr] > so])
            Noeud.child.append(noeud)
            noeud.parent = Noeud
        else:
            Noeud.split.pop(1)
            if len(np.unique(data[attr])) >= 2:
                for val in data[attr].value_counts().index:
                    Noeud.split.append(val)
                    noeud = Node(data.loc[data[attr] == val])
                    Noeud.child.append(noeud)
                    noeud.parent = Noeud
                    
        for child in Noeud.child:
                GenerationArbre(child, seuil)
    else:
        Noeud.leaf = True
    
    return Noeud