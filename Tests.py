
import random
from GenerationArbre import *
from Node import *
from sklearn.model_selection import train_test_split

"""Test sur IRIS"""
from sklearn.datasets import load_iris

"""Récupération des données et ajout d'une variable catégorielle fictive"""
iris = load_iris()
target = (iris.target).reshape(len(iris.target),1)
data = pd.DataFrame(np.concatenate((iris.data, target), axis = 1),
                   columns = ['sepl', 'sepw', 'petl', 'petw', 'spec'])
#data.insert(loc = 4, column = 'Cat', value = random.choices(['a','b'], k = 150))
#data.insert(loc = 4, column = 'Cat', value = np.repeat(['a','b','c'], 50))

"""Création d'un jeu de données d'entrainement et d'un jeu de données pour le test"""
 #data_train, data_test = train_test_split(data, test_size=0.1)

"""Entrainement du modèle"""
#Racine = Node(data_train)
#arbre = GenerationArbre(Racine, 1)

"""Prédictions et scores"""
scores = []
for nbtests in range(10):
    data_train, data_test = train_test_split(data, test_size=0.30)
    Racine = Node(data_train)
    arbre = GenerationArbre(Racine, 1)
    ypred = Prediction(arbre,data_test)
    scores.append(sum(ypred == data_test['spec'])/len(ypred))
print('Le score moyen est de :', np.mean(scores))

# """Test sur Examen"""
# data  = pd.DataFrame({"V1" : ["0", "0", "0", "0", "0", "I", "I", "I", "I", "I"],
#                       "V2" : ["1", "2", "1", "1","1", "2", "2", "2", "1", "1"],
#                       "V3" : ["B", "V", "B","V","B","V","B","V","B","V"],
#                       "Y"  : ["0", "0", "1", "1","1", "1", "0","1","0","1"]
#                       })

# data_train, data_test = train_test_split(data, test_size=0.20)

# Racine = Node(data_train)
# arbre = GenerationArbre(Racine, 0)

# ypred = Prediction(arbre,data_test)
# score = sum(ypred == data_test['Y'])/len(ypred)
# print('Le score est de :', score)