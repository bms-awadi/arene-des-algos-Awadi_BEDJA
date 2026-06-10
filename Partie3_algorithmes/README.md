# Arène des Algos

Notebook de comparaison d'algorithmes de ML sur 4 datasets réels.  
Chaque phase attaque un problème différent (régression, classification, clustering, NLP).  
La phase Fight produit un leaderboard final qui désigne le champion.

## Structure

```
Partie3_algorithmes/
├── arene_des_algos.ipynb   # Notebook principal
└── README.md               # Ce fichier
```

## Phases

| Phase | Problème | Dataset | Type |
|-------|----------|---------|------|
| A | Prix immobiliers | fetch_california_housing | Régression |
| B | Spam / Ham | SMS Spam Collection UCI | Classification |
| C | Logements Airbnb | Inside Airbnb (CSV) | À définir |
| Fight | Leaderboard | Tous | Comparaison |

## Champion

> À compléter en phase Fight.

## Lancer le notebook

```bash
jupyter notebook j3/arene_des_algos.ipynb
# ou ouvrir dans VS Code avec l'extension Jupyter
```

## Dépendances

```bash
pip install scikit-learn pandas numpy matplotlib
```