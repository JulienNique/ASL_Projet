
from Node import *
from DivisionAttribut2 import *
from RFDivisionAttribut import *

"""RFGenerationArbre pour Random Forest"""
def RFGenerationArbre(Noeud, seuil, p):
    #on initialise les data avec celles du noeud passé en argument
    data = Noeud.data
    #on récupère la variable attr pour la prochaine division, le seuil so si cette variable est numérique
    #et l'entropie MinE
    [attr, so, MinE] = RFDivisionAttribut(Noeud, p)
    #on teste que l'entropie est inférieure au seuil fixé pour l'arbre
    if(MinE <= seuil and MinE != 10):
        Noeud.split = [attr, so]
        if  (data[attr].dtypes == 'float64' or data[attr].dtypes == 'int64'):
            noeud = Node(data.loc[data[attr] <= so])
            Noeud.child.append(noeud)
            noeud.parent = Noeud    
            
            noeud = Node(data.loc[data[attr] > so])
            Noeud.child.append(noeud)
            noeud.parent = Noeud
        else:
            Noeud.split.pop(1)
            Noeud.var.remove(attr)
            if len(data[attr].value_counts().index) >= 2:
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