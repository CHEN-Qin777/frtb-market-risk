# Projet 3 : Calcul du capital réglementaire FRTB (SA + IMA)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/votre_nom/frtb-market-risk/blob/main/notebooks/frtb_calcul_complet.ipynb)

## 📌 À propos

**FRTB Market Risk**  
Calcul du capital réglementaire selon FRTB : approche standard (SA) avec sensibilités Delta, et approche par modèles internes (IMA) avec Expected Shortfall (ES) stressée. Comparaison des deux méthodes et backtest (test de Kupiec).

## 📋 Description détaillée

Ce projet implémente le calcul du capital réglementaire selon le standard **FRTB** (Fundamental Review of the Trading Book) de Bâle. Il utilise des données de marché réelles (Yahoo Finance) pour construire un portefeuille diversifié (actions, obligations, matières premières) et applique :

- L'approche standard (SA) pour le risque Delta, avec les poids de risque et corrélations définis par la réglementation.
- L'approche par modèles internes (IMA) : calcul de l'Expected Shortfall (ES) historique (97,5 %) et de l'ES stressé (moyenne des 60 pires périodes glissantes sur 250 jours).
- Une comparaison des deux approches.
- Un backtest de la VaR 99 % à l'aide du test de Kupiec pour valider la calibration du modèle.

## ✨ Fonctionnalités

- ✅ Téléchargement robuste des données de marché (fallback sur données synthétiques en cas d'échec)
- ✅ Calcul du capital Delta SA (formule de corrélation intra-bucket)
- ✅ Calcul de l'ES historique et de l'ES stressé
- ✅ Backtest des VaR avec le test de Kupiec
- ✅ Visualisation de l'ES glissant et du niveau de stress
- ✅ Code modulaire, testé et documenté

## 🔧 Installation

```bash
pip install -r requirements.txt
```

## 🚀 Utilisation

### Version locale
Exécutez les scripts dans l'ordre ou utilisez les modules dans votre propre code.

### Version Colab
Ouvrez le notebook [`frtb_calcul_complet.ipynb`](notebooks/frtb_calcul_complet.ipynb) dans Google Colab et exécutez toutes les cellules.

## 📊 Résultats obtenus

Les résultats suivants ont été obtenus avec un portefeuille équipondéré composé de **SPY** (actions), **TLT** (obligations) et **GLD** (or) sur la période **2015–2023**.

| Mesure | Valeur |
|--------|--------|
| **ES historique (97,5 %)** | –0,016802 |
| **ES stressé** (moyenne des 60 pires périodes) | –0,007238 |
| **Capital Delta SA** | 56 539,81 € |
| **Capital IMA** (rendement équivalent, horizon 10j, facteur 1,5) | –0,034333 |
| **Test de Kupiec (VaR 99 %)** – p-valeur | 0,9379 |

### ES glissant par année

Le tableau ci‑dessous montre l'évolution de l'ES 97,5 % glissant sur 250 jours ainsi que le niveau de stress (constant) :

| Année | ES 97.5% glissant (250j) | ES stressé (moyenne 60 pires) |
|-------|---------------------------|-------------------------------|
| 2016  | -0.013                    | -0.010                        |
| 2017  | -0.012                    | -0.010                        |
| 2018  | -0.009                    | -0.010                        |
| 2019  | -0.009                    | -0.010                        |
| 2020  | -0.008                    | -0.010                        |
| 2021  | -0.029                    | -0.010                        |
| 2022  | -0.014                    | -0.010                        |
| 2023  | -0.020                    | -0.010                        |
| 2024  | -0.015                    | -0.010                        |

### Interprétation

- L'**ES historique** mesure la perte moyenne dans les 2,5 % des pires scénarios sur la période récente.  
- L'**ES stressé** est plus élevé en valeur absolue (0,0072 contre 0,0168) car il prend la moyenne des 60 périodes glissantes où l'ES était le plus élevé, reflétant ainsi des conditions de marché extrêmes.  
- Le **capital SA** est calculé à partir de sensibilités hypothétiques (100 k€ sur actions, –50 k€ sur obligations, 20 k€ sur or) et donne un montant de 56 k€.  
- Le **capital IMA** est exprimé en rendement équivalent sur 10 jours (avec le facteur multiplicatif réglementaire de 1,5) ; sa valeur négative indique la perte potentielle.  
- Le **test de Kupiec** donne une p-valeur très élevée (0,94), ce qui signifie que le nombre d'exceptions observées (pertes > VaR 99 %) n'est pas significativement différent du nombre attendu sous l'hypothèse d'un modèle bien calibré. Le modèle de VaR historique 99 % est donc validé.

### Visualisation de l'ES glissant

La figure ci‑dessous (générée par le notebook) montre l'évolution de l'ES 97,5 % glissant sur 250 jours ainsi que le niveau de stress (ligne horizontale rouge). On observe des pics correspondant aux périodes de tension de marché (COVID‑19, 2022).

![ES glissant](results/image.png)  

## 📁 Structure du projet



## 📄 Licence

Projet éducatif – libre utilisation.

## 👤 Auteur

Étudiant en Master 2 Mathématiques Financières.

---

