# -*- coding: utf-8 -*-
"""Backtest des mesures de risque (test de Kupiec)."""
import numpy as np
from scipy.stats import chi2

def test_kupiec(pertes_reelles, var_prevues, niveau=0.99):
    """
    Test de Kupiec pour la couverture inconditionnelle.
    
    Paramètres
    ----------
    pertes_reelles : array
        Pertes réalisées (ou rendements négatifs)
    var_prevues : array
        VaR prévue (seuil négatif)
    niveau : float
        Niveau de confiance de la VaR
    
    Retour
    ------
    p_value : float
        p-valeur du test (H0 : modèle bien calibré)
    """
    # Compter les exceptions (pertes > VaR, i.e. pertes < var_prevues car var négative)
    exceptions = np.sum(pertes_reelles < var_prevues)
    n = len(pertes_reelles)
    p = 1 - niveau  # probabilité théorique d'exception
    if exceptions == 0 or exceptions == n:
        # Cas extrêmes, LR tend vers l'infini, H0 rejetée
        return 0.0
    LR = -2 * ((n - exceptions) * np.log(1 - p) + exceptions * np.log(p) -
               ((n - exceptions) * np.log(1 - exceptions/n) + exceptions * np.log(exceptions/n)))
    p_value = 1 - chi2.cdf(LR, 1)
    return p_value
