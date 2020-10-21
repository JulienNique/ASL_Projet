
import random
from Node import *
from RFGenerationArbre import *
from RFDivisionAttribut import *

#En arguments de la fonction RandomForest :
#n est le nombre d'arbres, p est le nombre de variables
#choisies aléatoirement à chaque division
def RandomForest(Noeud, seuil, n, p):
    forest = []
    #pour chaque arbre de la forêt
    for k in range(0,n):
        nrow = (Noeud.data).shape[0]
        #on effectue un bootstrap sur le jeu de données Noeud.data
        rows = random.choices(range(0,nrow), k = nrow)
        dataBS = Noeud.data.iloc[rows,:]
        #on crée la racine de l'arbre avec le bootstrap
        racine = Node(dataBS)
        #on entraîne l'arbre de classification
        arbre = RFGenerationArbre(racine, seuil, p)
        #on ajoute l'arbre à la forêt
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

