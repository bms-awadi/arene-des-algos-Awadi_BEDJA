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

### Phase 4 - Détection des outliers

Méthode utilisée :

- Visualisation par boxplots
- Détection via la règle IQR

Colonnes étudiées :

- tenure
- MonthlyCharges
- TotalCharges

Résultats :

Aucune des trois variables numériques ne présente de valeurs aberrantes selon le critère IQR.

| Variable | Nombre d'outliers |
|-----------|-----------|
| tenure | 0 |
| MonthlyCharges | 0 |
| TotalCharges | 0 |

Conclusion :

Aucune suppression ou transformation n'a été appliquée.
Les données numériques sont conservées telles quelles.

### Phase 5 - Corrélations et multicolinéarité

#### Corrélations observées

| Variable 1 | Variable 2 | Corrélation |
|------------|------------|-------------|
| tenure | TotalCharges | 0.825 |
| MonthlyCharges | TotalCharges | 0.651 |
| tenure | MonthlyCharges | 0.248 |

Une forte corrélation existe entre `TotalCharges` et `tenure`.

Cela est cohérent avec la définition métier :

TotalCharges ≈ tenure × MonthlyCharges

#### Analyse VIF

| Variable | VIF |
|-----------|------:|
| tenure | 6.32 |
| MonthlyCharges | 3.36 |
| TotalCharges | 8.07 |

Une multicolinéarité modérée à forte est observée.

#### Test de validation

Une variable dupliquée artificiellement (`tenure_clone`) produit un VIF infini, ce qui confirme le bon fonctionnement de l'analyse.

#### Décision

Les variables sont conservées.

Même si une redondance existe, elles portent une information métier utile et restent exploitables pour les modèles de classification envisagés.

### Phase 6 - Variables discriminantes

Trois approches ont été comparées :

- corrélation avec la cible
- information mutuelle
- importance Random Forest

Variables apparaissant régulièrement parmi les plus importantes :

- tenure
- Contract_Two year
- InternetService_Fiber optic
- MonthlyCharges
- TotalCharges
- PaymentMethod_Electronic check

Interprétation métier :

- les clients anciens churnent moins
- les contrats longs fidélisent davantage
- la fibre est associée à un risque de churn plus élevé
- les montants facturés jouent un rôle important

Observation :

Une variable fortement corrélée n'est pas nécessairement la plus importante pour un modèle prédictif.


### Phase 7 - PCA

Les données ont été standardisées avant application du PCA.

#### PCA à 2 composantes

Variance expliquée :

- PC1 : 33.18 %
- PC2 : 11.99 %

Variance cumulée :

- 45.17 %

#### Nombre de composantes nécessaires

Pour conserver 90 % de la variance :

- 15 composantes sont nécessaires

#### Interprétation

Le PCA permet une réduction importante de la dimension :

- 30 variables -> 2 composantes

Cependant, cette réduction conserve moins de la moitié de l'information du dataset.

Le PCA est donc utilisé ici comme outil d'exploration visuelle plutôt que comme remplacement des variables originales.

### Phase 8 - Préparation finale Machine Learning

Les données ont été séparées en :

- 80 % entraînement
- 20 % test

Le découpage utilise une stratification afin de conserver la proportion de churn observée dans le dataset original.

#### Standardisation

Un StandardScaler est entraîné uniquement sur les données d'entraînement.

Les données de test sont transformées avec ce même scaler.

Cette approche évite toute fuite de données entre les ensembles d'entraînement et de test.

#### Résultat

Dataset final prêt pour la phase de modélisation :

- X_train
- X_test
- y_train
- y_test