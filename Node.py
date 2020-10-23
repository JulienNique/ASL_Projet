
class Node:

    def __init__(self, data):
        self.data = data
        self.classeMaj = data.iloc[:,-1].value_counts().idxmax()
        self.child = []
        self.parent = None
        self.var = (data.columns.delete(-1)).tolist()
        self.split = []
        self.leaf = False

    def __str__(self):
        return str(self.data)

def ParcoursArbre(Arbre):
    print('Le noeud est une feuille :', Arbre.leaf)
    print('La classe majoritaire est :', Arbre.classeMaj)
    print('Le noeud est divisé par :', Arbre.split)
    print('\n')

    if Arbre.child != []:
        for child in Arbre.child:
            ParcoursArbre(child)
    
def Prediction(Arbre,X):
    ypred = []
    for index, x in X.iterrows():
        noeud = Arbre
        while noeud.leaf == False:
            if len(noeud.split) == 2:
                if x[noeud.split[0]] <= noeud.split[1]:
                    noeud = noeud.child[0]
                else:
                    noeud = noeud.child[1]
            elif x[noeud.split[0]] in noeud.split[1:]:
                pos = noeud.split[1:].index(x[noeud.split[0]])
                noeud = noeud.child[pos]
            else:
                break
                # try:
                #     pos = noeud.split[1:].index(x[noeud.split[0]])
                # except IndexError:
                #     pos = -1
                #     break
                # if pos != -1:
                #     noeud = noeud.child[pos]
                
        ypred.append(noeud.classeMaj)
    return ypred