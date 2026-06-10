## Phases

| Phase | Problème | Dataset | Type |
|-------|----------|---------|------|
| A | Prix immobiliers | fetch_california_housing | Régression |
| B | Segmentation AirBnB | Inside Airbnb Paris (CSV) | Clustering |
| C | Spam / Ham | SMS Spam Collection UCI | Classification |
| Fight | Leaderboard | Tous | Comparaison |

## Segments AirBnB Paris (Phase B)

| Segment | Profil | Nb listings | Nuits min moy | Capacité moy | Dispo moy |
|---------|--------|-------------|---------------|--------------|-----------|
| 0 | Touriste classique | 37 095 | 6.1 | 2.8 pers | 115j/an |
| 1 | Bail longue durée | 3 608 | 365.2 | 3.2 pers | 47j/an |
| 2 | Familial premium | 10 809 | 5.4 | 5.9 pers | 187j/an |

> k=3 retenu (silhouette avec scaling : 0.36).  
> Sans scaling : 0.65 — score artificiellement gonflé par la variance de `minimum_nights`.

## Champion

> À compléter en phase Fight.

## Lancer le notebook

```bash
# Créer l'environnement virtuel
python3.12 -m venv .venv
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate     # Windows

# Installer les dépendances
pip install scikit-learn pandas numpy matplotlib ipykernel requests

# Enregistrer le kernel
python -m ipykernel install --user --name=arene-algos --display-name "Arène des Algos (3.12)"

# Lancer le notebook
jupyter notebook arene_des_algos.ipynb
# ou ouvrir dans VS Code avec l'extension Jupyter
```

## Dépendances

```bash
pip install scikit-learn pandas numpy matplotlib ipykernel requests
```