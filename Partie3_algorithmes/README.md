# Arène des Algos

Notebook de comparaison d'algorithmes de ML sur 4 datasets réels.  
Chaque phase attaque un problème différent (régression, clustering, classification, classification binaire).  
La phase Fight produit un leaderboard final qui désigne le champion.

## Structure

```
Partie3_algorithmes/
├── arene_des_algos.ipynb   # Notebook principal
├── data/                   # Données locales (non commitées)
│   ├── listings.csv.gz     # Inside Airbnb Paris
│   ├── SMSSpamCollection   # SMS Spam Collection UCI
│   └── sonar.csv           # Sonar Mines vs Rocks UCI
└── README.md               # Ce fichier
```

## Phases

| Phase | Problème | Dataset | Type | Champion | Score |
|-------|----------|---------|------|----------|-------|
| A | Prix immobiliers | fetch_california_housing | Régression | RandomForest | R2=0.82 |
| B | Segmentation AirBnB | Inside Airbnb Paris | Clustering | KMeans k=3 | silhouette=0.36 |
| C | Spam / Ham | SMS Spam Collection UCI | Classification | NaiveBayes | F1=0.88 |
| D | Sonar mines/rochers | Sonar UCI | Classification binaire | SVC rbf | accuracy=0.93 |
| E | Leaderboard global | Tous | Comparaison | SVC rbf | 2/3 datasets |

## Segments AirBnB Paris (Phase B)

| Segment | Profil | Nb listings | Nuits min moy | Capacité moy | Dispo moy |
|---------|--------|-------------|---------------|--------------|-----------|
| 0 | Touriste classique | 37 095 | 6.1 | 2.8 pers | 115j/an |
| 1 | Bail longue durée | 3 608 | 365.2 | 3.2 pers | 47j/an |
| 2 | Familial premium | 10 809 | 5.4 | 5.9 pers | 187j/an |

> k=3 retenu (silhouette avec scaling : 0.36).  
> Sans scaling : 0.65 score artificiellement gonflé par la variance de `minimum_nights`.

## Champion

**SVC rbf** : vainqueur sur 2/3 datasets (Sonar accuracy=0.93, Spam F1=0.92).

| Dataset | Champion | Score | Temps entraînement |
|---------|----------|-------|--------------------|
| Sonar | SVC rbf | accuracy=0.93 | 0.003s |
| Spam | SVC rbf | F1=0.92 | 0.906s |
| California Housing | RandomForest | R2=0.81 | 17.7s |

**Pourquoi SVC rbf ?**  
Excelle dans les espaces de grande dimension (60 variables sonar, TF-IDF spam).  
Sur gros volumes (20k lignes housing), RandomForest devient plus pertinent SVC serait trop lent à entraîner.

## Lancer le notebook

```bash
# Créer l'environnement virtuel
python3.12 -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows

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
