# -*- coding: utf-8 -*-
"""Téléchargement robuste des données de marché depuis Yahoo Finance."""
import yfinance as yf
import pandas as pd
import numpy as np

def telecharger_donnees(tickers, debut, fin):
    """
    Télécharge les prix ajustés si disponibles, sinon les prix 'Close'.
    Gère les cas où le retour est un DataFrame simple ou MultiIndex.
    En cas d'échec, génère des données synthétiques.
    """
    try:
        data = yf.download(tickers, start=debut, end=fin, progress=False)
        if data.empty:
            raise ValueError("Aucune donnée reçue.")

        # Essayer d'extraire les prix ajustés ou de clôture
        if 'Adj Close' in data.columns:
            prices = data['Adj Close']
        elif 'Close' in data.columns:
            prices = data['Close']
        elif isinstance(data.columns, pd.MultiIndex) and 'Close' in data.columns.get_level_values(0):
            prices = data['Close']
        else:
            # Si aucune colonne reconnue, prendre la première colonne disponible
            prices = data.iloc[:, 0]
            print("Avertissement : colonne 'Adj Close' ou 'Close' non trouvée, utilisation de la première colonne.")

        # S'assurer que c'est un DataFrame (si un seul ticker, yfinance peut retourner une Series)
        if isinstance(prices, pd.Series):
            prices = prices.to_frame(name=tickers[0] if isinstance(tickers, list) else tickers)
        return prices

    except Exception as e:
        print(f"Erreur de téléchargement : {e}")
        print("Utilisation de données synthétiques.")
        return generer_donnees_synthetiques(tickers, debut, fin)

def generer_donnees_synthetiques(tickers, debut, fin):
    """Génère des données de prix synthétiques (mouvement brownien géométrique)."""
    dates = pd.date_range(start=debut, end=fin, freq='B')
    prix = pd.DataFrame(index=dates)
    for t in tickers:
        prix[t] = 100 * np.exp(np.random.randn(len(dates)).cumsum() / 100)
    return prix
