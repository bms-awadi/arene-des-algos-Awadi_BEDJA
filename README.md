# Arene des Algos — Awadi & Bedja

Projet ML de bout en bout : pipeline supervisé, classement d'algorithmes, clustering non-supervisé, scaling, visualisations.

## Ce que ce repo contient

- Un notebook Jupyter avec le pipeline complet (chargement, split, entraînement, évaluation)
- Une Arène : plusieurs algorithmes de classification comparés sur le même découpage train/test
- Une bascule non-supervisée (KMeans) pour voir si la structure existe sans les étiquettes
- Des visualisations (barres d'accuracy, matrice de confusion du champion)
- Une démo data leakage : ce qui se passe quand on triche avec le StandardScaler
- Ce README : le classement final, le champion retenu, et pourquoi

## Datasets

- `breast_cancer` (sklearn) : 569 patients, 30 mesures, tumeur bénigne ou maligne
- `wine` (sklearn) : 178 vins, 13 mesures, 3 cépages (classification multi-classe)

## Algorithmes comparés

- Régression logistique
- Arbre de décision
- K-Nearest Neighbors (KNN)

## Structure du repo

```
README.md
arene_algos_ml.ipynb
```

## Classement final

> A compléter après la Phase 8.

## Champion retenu

> A compléter après la Phase 8.
