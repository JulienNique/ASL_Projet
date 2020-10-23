
from Node import *
from DivisionAttribut2 import *
from RFDivisionAttribut import *

"""GenerationArbre"""
def GenerationArbre(Noeud, seuil):
    #on initialise les data avec celles du noeud passé en argument
    data = Noeud.data
    #on récupère la variable attr pour la prochaine division, le seuil so si cette variable est numérique
    #et l'entropie MinE
    [attr, so, MinE] = DivisionAttribut(data)
    #on teste que l'entropie est inférieure au seuil fixé pour l'arbre
    if(MinE <= seuil):
        #on met à jour les informations du node Noeud et on crée les noeuds descendants
        Noeud.split = [attr, so]
        #pour une variable numérique
        if  (data[attr].dtypes == 'float64' or data[attr].dtypes == 'int64'):
            noeud = Node(data.loc[data[attr] <= so])
            Noeud.child.append(noeud)
            noeud.parent = Noeud    
            
            noeud = Node(data.loc[data[attr] > so])
            Noeud.child.append(noeud)
            noeud.parent = Noeud
        #pour une variable qualitative
        else:
            Noeud.split.pop(1)
            if len(data[attr].value_counts().index) >= 2:
                for val in data[attr].value_counts().index:
                    Noeud.split.append(val)
                    noeud = Node(data.loc[data[attr] == val])
                    Noeud.child.append(noeud)
                    noeud.parent = Noeud
        
        #on appelle récursivement la fonction pour créer les noeuds suivants
        for child in Noeud.child:
            GenerationArbre(child, seuil)
    #si le noeud courant n'a pas de descendants, c'est une feuille par définition
    else:
        Noeud.leaf = True
    
    return Noeud


