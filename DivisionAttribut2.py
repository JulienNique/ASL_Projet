{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Untitled24.ipynb",
      "provenance": [],
      "authorship_tag": "ABX9TyOH8TBx3eBUxM4R7nNOs5zu",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/JulienNique/ASL_Projet/blob/main/DivisionAttribut2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "id": "riTTKcfFkNMV"
      },
      "source": [
        "def DivisionAttribut2(data):\n",
        "    global Einf, Esup, E, j\n",
        "    target = data.columns[-1]\n",
        "    ncol = data.shape[1]\n",
        "    MinE = 10 ; so = []\n",
        "    for col_index in range(ncol-1):\n",
        "      #print(data.columns[col_index])\n",
        "      unique_values = np.unique(data.iloc[:,col_index]) #get les val uniq\n",
        "      if data.iloc[:,col_index].dtypes == \"float64\":\n",
        "        #print(data.columns[col_index], \"est quanti\")\n",
        "      \n",
        "        for i in range(1,len(unique_values)):\n",
        "          seuil = (unique_values[i] + unique_values[i-1])/2\n",
        "          dataSup = data[data.iloc[:,col_index]>seuil]\n",
        "          targetSup = dataSup.iloc[:,-1]\n",
        "          dataInf = data[data.iloc[:,col_index]<=seuil]\n",
        "          targetInf = dataInf.iloc[:,-1]\n",
        "          tinf = targetInf.value_counts()\n",
        "          tsup = targetSup.value_counts()\n",
        "          Ninf = np.sum(tinf) ; Nsup = np.sum(tsup) ; N = Ninf + Nsup\n",
        "          if (Ninf != 0):\n",
        "            Einf = 0\n",
        "            for n in tinf:\n",
        "              Einf = Einf - n/Ninf*np.log2(n/Ninf)\n",
        "          if (Nsup != 0):\n",
        "            Esup = 0 \n",
        "            for n in tsup:\n",
        "              Esup = Esup - n/Nsup*np.log2(n/Nsup)\n",
        "          E = Ninf/N*Einf + Nsup/N*Esup\n",
        "          if (E < MinE):\n",
        "            MinE = E ; j = data.columns[col_index] ; so = seuil\n",
        "    \n",
        "    \n",
        "      else:\n",
        "        attr = data.columns[col_index]\n",
        "        #print(attr, 'est quali')\n",
        "        if (len(np.unique(data[attr])) >= 2):\n",
        "          E = 0\n",
        "          N = len(data[attr])\n",
        "          for s in data[attr].value_counts().index:\n",
        "            t = data.loc[data[attr] == s, target].value_counts()\n",
        "            Nt = np.sum(t)\n",
        "            for n in t:\n",
        "              E = E -Nt/N*(n/Nt*np.log2(n/Nt))\n",
        "          if (E < MinE):\n",
        "            MinE = E ; j = attr ; so = 'nn'\n",
        "    return [j, so, MinE]"
      ],
      "execution_count": 1,
      "outputs": []
    }
  ]
}