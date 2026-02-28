# -*- coding: utf-8 -*-
"""Nettoyage et calcul des rendements."""
import pandas as pd
import numpy as np

def calculer_rendements(prix, methode='log'):
    """Calcule les rendements (log ou simples)."""
    if methode == 'log':
        rendements = np.log(prix / prix.shift(1))
    else:
        rendements = prix.pct_change()
    return rendements.dropna()

def nettoyer_donnees(prix):
    """Supprime les lignes avec des NaN et les colonnes avec trop de NaN."""
    prix = prix.dropna(axis=0, how='any')
    prix = prix.dropna(axis=1, thresh=0.7 * len(prix))
    return prix
