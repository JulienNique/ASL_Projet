
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
data_train, data_test = train_test_split(data, test_size=0.10)

noeud = Node(data_train)
forest = RandomForest(noeud, 1, 1, 4)

ypred = RFPrediction(forest, data_test)
score = sum(ypred == data_test['Survived'])/len(ypred)
print('Le score est de :', score)

# a = [1, 2, 3]
# try:
#     pos = a.index(10)
# except ValueError:
#     print('not found')