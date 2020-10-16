# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 11:54:58 2020


@author: jnique
"""

import pandas as pd
import numpy as np
import random

def RFDivisionAttribut(Noeud, p):
    global Einf, Esup, E, j
    data = Noeud.data
    target = data.columns[-1]
    MinE = 10 ; so = []
    for attr in np.unique(random.choices(Noeud.var, k = p)):
        if data[attr].dtypes == 'float64': #la variable est quantitative
            for s in data[attr].value_counts().index:
                tinf = data.loc[data[attr] <= s, target].value_counts()
                tsup = data.loc[data[attr] > s, target].value_counts()
                #calcul de l'entropie associée au seuil s
                Ninf = np.sum(tinf) ; Nsup = np.sum(tsup) ; N = Ninf + Nsup
                if (Ninf != 0):
                    Einf = 0 
                    for n in tinf:
                        Einf = Einf - n/Ninf*np.log2(n/Ninf)
                if (Nsup != 0):
                    Esup = 0 
                    for n in tsup:
                        Esup = Esup - n/Nsup*np.log2(n/Nsup)
                E = Ninf/N*Einf + Nsup/N*Esup
                if (E < MinE and s < max(data[attr])):
                    MinE = E ; j = attr ; so = s
        else: #la variable est qualitative
            if (len(np.unique(data[attr])) >= 2):
                E = 0
                N = len(data[attr])
                for s in data[attr].value_counts().index:
                    t = list((data.loc[data[attr] == s, target]).value_counts())
                    Nt = np.sum(t)
                    for n in t:
                        E = E -Nt/N*(n/Nt*np.log2(n/Nt))
                if (E < MinE):
                    MinE = E ; j = attr
        
    return [j, so, MinE]


def RFDivisionAttribut2(Noeud, p):
    global Einf, Esup, E, j
    data = Noeud.data
    target = data.columns[-1]
    MinE = 10 ; so = []
    for attr in np.unique(random.choices(Noeud.var, k = p)):
        if data[attr].dtypes == 'float64': #la variable est quantitative
            unique_values = np.unique(data[attr])
            for i in range(1,len(unique_values)):
                s = (unique_values[i] + unique_values[i-1])/2
                targetSup = data.loc[data[attr] > s, target]
                targetInf = data.loc[data[attr] <= s, target]
                tinf = targetInf.value_counts()
                tsup = targetSup.value_counts()      
                #calcul de l'entropie associée au seuil s
                Ninf = np.sum(tinf) ; Nsup = np.sum(tsup) ; N = Ninf + Nsup
                if (Ninf != 0):
                    Einf = 0 
                    for n in tinf:
                        Einf = Einf - n/Ninf*np.log2(n/Ninf)
                if (Nsup != 0):
                    Esup = 0 
                    for n in tsup:
                        Esup = Esup - n/Nsup*np.log2(n/Nsup)
                E = Ninf/N*Einf + Nsup/N*Esup
                if (E < MinE):
                    MinE = E ; j = attr ; so = s
        else:
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