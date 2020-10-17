import pandas as pd
import numpy as np

#la fonction Division Attribut2 prend en argument les données du noeud courant dans la construction de l'arbre
def DivisionAttribut2(data):
    global Einf, Esup, E
    target = data.columns[-1] #target contient la variable cible
    ncol = data.shape[1] #le nombre de colonnes dans le dataframe data
    j = [] ; MinE = 10 ; so = [] #initialisation des valeurs de sortie
    #on teste si il y a au moins deux modalités dans la target
    if len(np.unique(data.iloc[:,-1])) >= 2:
        #on parcourt toutes les variables descriptives
        for col_index in range(ncol-1):
          #on récupère les modalités/valeurs de la variable courante
          unique_values = np.unique(data.iloc[:,col_index])
          #on teste si la variable est numérique
          if data.iloc[:,col_index].dtypes == "float64":
            #on parcourt alors les valeurs par ordre croissant
            for i in range(1,len(unique_values)):
              #chaque seuil correspond à la moyenne de deux valeurs consécutives
              seuil = (unique_values[i] + unique_values[i-1])/2
              #on divise le dataframe data en deux et on calcule l'entropie pour la cible target
              dataSup = data[data.iloc[:,col_index]>seuil]
              targetSup = dataSup.iloc[:,-1]
              dataInf = data[data.iloc[:,col_index]<=seuil]
              targetInf = dataInf.iloc[:,-1]
              tinf = targetInf.value_counts()
              tsup = targetSup.value_counts()
              Ninf = np.sum(tinf) ; Nsup = np.sum(tsup) ; N = Ninf + Nsup
              Einf = 0
              for n in tinf:
                Einf = Einf - n/Ninf*np.log2(n/Ninf)
              Esup = 0 
              for n in tsup:
                Esup = Esup - n/Nsup*np.log2(n/Nsup)
              E = Ninf/N*Einf + Nsup/N*Esup
              #on teste si l'entropie est meilleure que la précédente calculée
              if (E < MinE):
                #on met à jour la variable j qui contient le nom de la variable qui réalise le meilleur split,
                #la valeur de l'entropie correspondante et le seuil
                MinE = E ; j = data.columns[col_index] ; so = seuil
        
        
          else: #la variable est qualitative
            attr = data.columns[col_index]
            #on teste que la variable contient au moins deux modalités
            if (len(np.unique(data[attr])) >= 2):
              E = 0
              N = len(data[attr])
              for s in data[attr].value_counts().index:
                t = data.loc[data[attr] == s, target].value_counts()
                Nt = np.sum(t)
                for n in t:
                  E = E -Nt/N*(n/Nt*np.log2(n/Nt))
              if (E < MinE):
                MinE = E ; j = attr ; so = 'nn' #on met à jour la variable j
        
    return [j, so, MinE]
