# -*- coding: utf-8 -*-
"""
Created on Fri Oct 16 08:46:30 2020

@author: julien
"""

from Node import *
#from DivisionAttribut import *
from DivisionAttribut2 import *
from RFDivisionAttribut import *

"""GenerationArbre"""
def GenerationArbre(Noeud, seuil):
    data = Noeud.data #on initialise les data avec celles du noeud courant
    [attr, so, MinE] = DivisionAttribut2(data) #on récupère la variable attr pour la prochaine division
    #print([attr, so, MinE])
    if(MinE <= seuil and MinE != 10): #on teste que l'entropie est inférieure au seuil fixé pour l'arbre
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
                #print('creation de child')
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


"""RFGenerationArbre pour Random Forest"""
def RFGenerationArbre(Noeud, seuil, p):
    data = Noeud.data
    [attr, so, MinE] = RFDivisionAttribut2(Noeud, p)
    #print([attr, so, MinE])
    if(MinE <= seuil and MinE != 10):
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
            Noeud.var.remove(attr)
            if len(np.unique(data[attr])) >= 2:
                for val in data[attr].value_counts().index:
                    Noeud.split.append(val)
                    noeud = Node(data.loc[data[attr] == val])
                    Noeud.child.append(noeud)
                    noeud.parent = Noeud
                    
        for child in Noeud.child:
            RFGenerationArbre(child, seuil, p)
    else:
        Noeud.leaf = True
    
    return Noeud