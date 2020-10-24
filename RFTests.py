
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris 
from RandomForest import *

#iris = load_iris()
#target = (iris.target).reshape(len(iris.target),1)
#data = pd.DataFrame(np.concatenate((iris.data, target), axis = 1),
#                    columns = ['sepl', 'sepw', 'petl', 'petw', 'spec'])

#Titanic
data = pd.read_csv("C:/Users/julien/Google Drive/DataSience/Machine Learning/Titanic/all/train.csv", sep=";")
data.dropna(how='all', inplace = True)

data = data[['Age','Pclass','Sex','Embarked','Survived']]
data_train, data_test = train_test_split(data, test_size=0.30)

scores = []
for nbtests in range(10):
    racine = Node(data_train)
    forest = RandomForest(racine, 1, 10, 2)
    ypred = RFPrediction(forest, data_test)
    score = sum(ypred == data_test['Survived'])/len(ypred)
    scores.append(score)
print('Le score moyen est de :', np.mean(scores))