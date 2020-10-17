import pandas as pd
import numpy as np

#La fonction Division Attribut2 prend en argument les données du noeud courant dans la construction de l'arbre
def DivisionAttribut2(data):
    global Einf, Esup, E
    target = data.columns[-1] #target contient la variable cible
    ncol = data.shape[1]
    j = [] ; MinE = 10 ; so = []
    if len(np.unique(data.iloc[:,-1])) >= 2: #on teste si il y a au moins deux modalités dans la target
        for col_index in range(ncol-1): #on parcourt toutes les variables descriptives
          unique_values = np.unique(data.iloc[:,col_index]) #on récupère les modalités/valeurs de la variable courante
          if data.iloc[:,col_index].dtypes == "float64": #on teste si la variable est numérique
            for i in range(1,len(unique_values)): #on parcourt les valeurs par ordre croissant
              seuil = (unique_values[i] + unique_values[i-1])/2 #chaque seuil correspond à la moyenne de deux valeurs consécutives
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
              if (E < MinE):
                MinE = E ; j = data.columns[col_index] ; so = seuil #on met à jour la variable j qui contient le nom de la variable qui réalise le meilleur split
        
        
          else: #la variable est qualitative
            attr = data.columns[col_index]
            if (len(np.unique(data[attr])) >= 2): #on teste que la variable contient au moins deux modalités
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
