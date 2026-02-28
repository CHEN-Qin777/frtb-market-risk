# -*- coding: utf-8 -*-
"""Calcul de l'Expected Shortfall pour l'approche par modèles internes."""
import numpy as np

def es_historique(rendements, niveau=0.975):
    """Calcule l'Expected Shortfall historique."""
    var = np.percentile(rendements, 100 * (1 - niveau))
    es = rendements[rendements <= var].mean()
    return es

def es_stresse(rendements, fenetre=250, niveau=0.975, n_stresse=60):
    """
    Calcule l'ES en période de stress : moyenne des n_stresse plus grandes
    valeurs de ES glissant sur fenêtre.
    """
    es_glissant = []
    for i in range(fenetre, len(rendements)):
        es = es_historique(rendements[i-fenetre:i], niveau)
        es_glissant.append(es)
    es_glissant = np.array(es_glissant)
    # Prendre la moyenne des n_stresse plus grandes valeurs
    es_stress = np.mean(np.sort(es_glissant)[-n_stresse:])
    return es_stress
