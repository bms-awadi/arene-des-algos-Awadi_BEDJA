# Telco Customer Churn

## Objectif

Préparer un dataset réel de churn client afin d'obtenir une base propre, encodée et prête pour la modélisation.

## Dataset

Telco Customer Churn Dataset

- ~7000 clients
- 21 colonnes
- cible : Churn

## Étapes prévues

- Chargement des données
- Audit qualité
- Nettoyage
- Encodage
- Détection des outliers
- Corrélations et multicolinéarité
- Sélection de variables
- Split et scaling
- Préparation finale pour le Machine Learning

### chargement des données

Le dataset est téléchargé automatiquement via kagglehub puis copié dans le dossier `data/`.

### Phase 1 - Audit qualité
Trois scénarios ont été testés :

#### Cas normal

Dataset complet : aucune anomalie détectée.

#### Cas limite

Audit exécuté sur un dataset ne contenant qu'une seule classe
de churn (Yes puis No).

Le rapport reste fonctionnel et affiche correctement 100 %.

#### Cas adversarial

Le dataset présente un déséquilibre de classes :

- No : 73.46 %
- Yes : 26.54 %

Cette information est visible immédiatement dans le rapport
et sera prise en compte lors de l'évaluation des modèles.

### Phase 2 - Réparation de TotalCharges

La colonne `TotalCharges` était stockée au format texte.

Investigation :

- type initial : `str`
- 11 valeurs contenant uniquement un espace `" "`
- conversion via `pd.to_numeric(errors="coerce")`

Résultat :

- 11 valeurs manquantes cachées détectées
- imputation par la médiane (1397.47)
- conversion finale en `float64`
- aucun NaN restant

Pourquoi l'imputation ?

Les 11 lignes représentent moins de 0.2 % du dataset.
L'imputation permet de conserver toutes les observations tout en limitant l'influence des valeurs extrêmes grâce à l'utilisation de la médiane.

### Phase 3 - Encodage des variables catégorielles

Actions réalisées :

- suppression de la colonne `customerID`
- encodage One-Hot des variables catégorielles
- transformation du dataset en données 100 % numériques

Résultat :

- dimensions avant : (7043, 20)
- dimensions après : (7043, 31)
- aucune colonne de type object restante

Pourquoi supprimer customerID ?

Chaque client possède un identifiant unique.

Un encodage One-Hot aurait créé 7043 colonnes supplémentaires sans apporter d'information utile au modèle.

Pourquoi utiliser One-Hot sur Contract ?

Les modalités possèdent un ordre apparent :

- Month-to-month
- One year
- Two year

Cependant, un encodage ordinal imposerait une distance artificielle entre les catégories.

Le One-Hot Encoding évite cette hypothèse et reste plus robuste pour les modèles classiques.