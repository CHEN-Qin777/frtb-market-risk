# -*- coding: utf-8 -*-
"""Calcul du capital Delta selon l'approche standard FRTB."""
import numpy as np

def sa_delta_capital(sensitivities, risk_weights, correlations):
    """
    Calcule le capital Delta pour un bucket.
    
    Paramètres
    ----------
    sensitivities : array-like
        Sensibilités aux facteurs de risque (DV01, etc.)
    risk_weights : array-like
        Poids de risque réglementaires (RW)
    correlations : 2D array
        Matrice de corrélation intra-bucket
    
    Retour
    ------
    float : capital Delta
    """
    sw = np.array(sensitivities) * np.array(risk_weights)
    K = np.sqrt(np.dot(sw, np.dot(correlations, sw)))
    return K
