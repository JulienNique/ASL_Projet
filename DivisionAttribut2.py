import pandas as pd
import numpy as np

def DivisionAttribut2(data):
    global Einf, Esup, E
    target = data.columns[-1]
    ncol = data.shape[1]
    j = [] ; MinE = 10 ; so = []
    if len(np.unique(data.iloc[:,-1])) >= 2: #on teste si il y a au moins deux targets   
        for col_index in range(ncol-1):
          unique_values = np.unique(data.iloc[:,col_index]) #get les val uniq
          if data.iloc[:,col_index].dtypes == "float64":
            #print(data.columns[col_index], "est quanti")
          
            for i in range(1,len(unique_values)):
              seuil = (unique_values[i] + unique_values[i-1])/2
              dataSup = data[data.iloc[:,col_index]>seuil]
              targetSup = dataSup.iloc[:,-1]
              dataInf = data[data.iloc[:,col_index]<=seuil]
              targetInf = dataInf.iloc[:,-1]
              tinf = targetInf.value_counts()
              tsup = targetSup.value_counts()
              Ninf = np.sum(tinf) ; Nsup = np.sum(tsup) ; N = Ninf + Nsup
              if (Ninf != 0 and Nsup != 0):
                Einf = 0
                for n in tinf:
                  Einf = Einf - n/Ninf*np.log2(n/Ninf)
                Esup = 0 
                for n in tsup:
                  Esup = Esup - n/Nsup*np.log2(n/Nsup)
                E = Ninf/N*Einf + Nsup/N*Esup
                if (E < MinE):
                    MinE = E ; j = data.columns[col_index] ; so = seuil
        
        
          else:
            attr = data.columns[col_index]
            if (len(np.unique(data[attr])) >= 2):
              E = 0
              N = len(data[attr])
              for s in data[attr].value_counts().index:
                t = data.loc[data[attr] == s, target].value_counts()
                Nt = np.sum(t)
                for n in t:
                  E = E -Nt/N*(n/Nt*np.log2(n/Nt))
              if (E < MinE):
                MinE = E ; j = attr ; so = 'nn'
        
    return [j, so, MinE]
