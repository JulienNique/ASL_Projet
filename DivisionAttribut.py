# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 11:54:58 2020

@author: jnique
"""

import pandas as pd
import numpy as np

def DivisionAttribut(data):
    global Einf, Esup, E, j
    target = data.columns[-1]
    MinE = 10 ; so = []
    for attr in data.columns.delete(-1):
        if data[attr].dtypes == 'float64':
            for s in data[attr].value_counts().index:
                #séparation en deux
                tinf = list((data.loc[data[attr] <= s, target]).value_counts())
                tsup = list((data.loc[data[attr] > s, target]).value_counts())
                #calcul de l'entropie
                Ninf = np.sum(tinf) ; Nsup = np.sum(tsup) ; N = Ninf + Nsup
                if (Ninf != 0):
                    Einf = 0 
                    for n in tinf:
                        Einf = Einf - n/Ninf*np.log(n/Ninf)
                if (Nsup != 0):
                    Esup = 0 
                    for n in tsup:
                        Esup = Esup - n/Nsup*np.log(n/Nsup)
                E = Ninf/N*Einf + Nsup/N*Esup
                if (E < MinE):
                    MinE = E ; j = attr ; so = s
        else:
            if (len(np.unique(data[attr])) >= 2):
                E = 0
                N = len(data[attr])
                for s in data[attr].value_counts().index:
                    t = list((data.loc[data[attr] == s, target]).value_counts())
                    Nt = np.sum(t)
                    for n in t:
                        E = E - n/Nt*np.log(n/Nt)
                    E = Nt/N*E + E
                if (E < MinE):
                    MinE = E ; j = attr
        
    return [j, so, MinE]