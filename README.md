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

### breast_cancer (569 patients, 30 mesures, 2 classes)

| Rang | Algorithme            | Brut  | Avec scaling |
|------|-----------------------|-------|--------------|
| 1    | Régression logistique | 95.6% | **97.4%**    |
| 2    | KNN                   | 95.6% | 94.7%        |
| 3    | Arbre de décision     | 94.7% | 94.7%        |

### wine (178 vins, 13 mesures, 3 classes)

| Rang | Algorithme            | Accuracy |
|------|-----------------------|----------|
| 1    | Régression logistique | 100.0%   |
| 2    | Arbre de décision     | 94.4%    |
| 3    | KNN                   | 72.2%    |

KNN chute à 72.2% sur wine sans scaling : le dataset a des features avec des échelles très différentes (ex : alcool ≈ 12-14 vs proline ≈ 500-1700). KNN raisonne par distances, il est aveuglé par les grandes valeurs.

### Clustering non-supervisé (breast_cancer)

KMeans à 2 clusters, sans jamais voir les étiquettes : **85.4% d'accord** avec les vraies classes. La structure bénigne/maligne existe dans les données — ce n'est pas de la chance.

## Champion retenu

**Régression logistique avec StandardScaler** : 97.4% sur breast_cancer, 100% sur wine.

Pourquoi ce choix et pas un autre :

- **Accuracy** : meilleure sur les deux datasets, cohérente après scaling
- **Explicabilité** : les coefficients du modèle indiquent directement quelles mesures pèsent le plus dans la décision
- **Type d'erreurs** : sur breast_cancer, le Régression logistique fait moins de faux négatifs (tumeurs malignes ratées) que l'arbre.
- **Vitesse** : entraînement quasi-instantané sur ces volumes, déployable facilement

Limite principale : nécessite un StandardScaler ajusté sur le train seul. Sans scaling, il perd 1.8pt et peut ne pas converger. L'arbre de décision n'a pas ce prérequis.

## Note sur le data leakage

Ajuster le scaler sur tout X avant le split gonfle artificiellement l'accuracy. Sur breast_cancer l'effet est nul (dataset homogène), mais sur un dataset réel avec une distribution asymétrique train/test, ce mensonge peut atteindre plusieurs points et faire passer un modèle moyen pour un faux champion en production.

**Règle à graver : on ajuste toujours le scaler sur le train uniquement.**
