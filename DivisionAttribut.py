# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 11:54:58 2020

@author: jnique
"""

import pandas as pd
import numpy as np

def DivisionAttribut(data):
    global Einf, Esup, Et, E, j
    target = data.columns[-1]
    MinE = 10 ; so = []
    for attr in data.columns.delete(-1):
        if data[attr].dtypes == 'float64': #la variable est quantitative
            for s in data[attr].value_counts().index:
                tinf = list((data.loc[data[attr] <= s, target]).value_counts())
                tsup = list((data.loc[data[attr] > s, target]).value_counts())
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
        else: #la variable est qualitative
            if (len(np.unique(data[attr])) >= 2):
                E = 0 ; Et = 0
                N = len(data[attr])
                for s in data[attr].value_counts().index:
                    t = list((data.loc[data[attr] == s, target]).value_counts())
                    Nt = np.sum(t)
                    for n in t:
                        Et = Et - n/Nt*np.log2(n/Nt)
                    E = Nt/N*Et + E
                if (E < MinE):
                    MinE = E ; j = attr
        
    return [j, so, MinE]