# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 10:43:27 2020

@author: jnique
"""

class Node:

    def __init__(self, data):
        self.data = data
        self.child = []
        self.parent = None
        self.classeMaj = data.iloc[:,-1].value_counts().idxmax()
        self.split = []
        self.var = (data.columns.delete(-1)).tolist()
        self.leaf = False

    def __str__(self):
        return str(self.data)

def ParcoursArbre(Arbre):
    print(Arbre.leaf)
    print(Arbre.split)
    print(Arbre.var)
#    print(Arbre.classeMaj
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
                pos = noeud.split[1:].index(x[noeud.split[0]])
                #print(pos)
                noeud = noeud.child[pos]
                
        ypred.append(noeud.classeMaj)
    return ypred