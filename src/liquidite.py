# -*- coding: utf-8 -*-
"""Ajustement de liquidité selon FRTB (simplifié)."""
def ajustement_liquidite(horizon_base, facteur_liquidite):
    """
    Ajuste l'horizon de liquidité pour un facteur de risque donné.
    """
    return horizon_base * facteur_liquidite
