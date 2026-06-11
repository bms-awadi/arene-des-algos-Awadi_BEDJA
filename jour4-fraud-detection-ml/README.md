# Fraud Detection ML : Détection de fraude bancaire

## Contexte métier

Une banque de détail traite **10 000 transactions par jour**. Environ **1% sont frauduleuses** (dataset fortement déséquilibré). L'enjeu n'est **pas l'accuracy**, un modèle qui dit toujours "pas de fraude" atteint 99% d'accuracy tout en ratant 100% des fraudes.

### Coût métier des erreurs

| Erreur | Type | Coût |
|--------|------|------|
| Fraude non détectée | Faux négatif (FN) | **Très élevé**, argent perdu |
| Transaction légitime bloquée | Faux positif (FP) | Modéré, friction client |

**Métrique cible : Recall élevé** (minimiser les FN), avec un coût métier total = `FN × cout_fn + FP × cout_fp`.

---

## Objectif du projet

Comparer plusieurs modèles de classification sur un dataset de fraude bancaire réel (Kaggle), en évaluant chacun **non pas sur l'accuracy mais sur le coût métier réel**.

Démontrer qu'un modèle "moins précis" peut coûter 2-3× moins cher en fraudes ratées.

---

## Phases du projet

| Phase | Description |
|-------|-------------|
| **0** | Setup du projet, dataset Kaggle, README |
| **1** | EDA, scaling Amount/Time, split train/val/test stratifié |
| **2** | Bootstrap OOB, stabilité modèle, accuracy trompeuse confirmée sur dataset déséquilibré |
| **3** | Validation croisée k-fold, LOO impossible sur déséquilibre, StratifiedKFold vs standard |
| **4** | Métriques métier, coût FN/FP, RF champion coût 294 vs LR 471 vs paresseux 990 |
| **5** | Sérialisation RF champion, API Flask predict fraude/legitime, checkpoints validés |
| **6** | WebApp Streamlit, sélection dataset ou import CSV, batch 6/6 correct sur test samples |

---

## Résultats

| Modèle | Précision | Recall | F1 | Coût métier |
|--------|-----------|--------|----|-------------|
| Paresseux (always 0) | 0.00 | 0.00 | 0.00 | 990 |
| Logistic Regression | 0.83 | 0.54 | 0.65 | 471 |
| **Random Forest** | **0.95** | **0.71** | **0.81** | **294** |

**Champion : Random Forest**, coût métier 294, soit 3.4× moins cher que le modèle paresseux et 1.6× moins cher que la régression logistique.

Validation sur batch de 6 transactions (3 légitimes, 3 fraudes) : **6/6 prédictions correctes**.

---

## Dataset

Source : [Kaggle : Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)
Téléchargement via `kagglehub`.

- 284 807 transactions, 492 fraudes (0.17%)
- Features anonymisées V1-V28 (PCA) + Amount + Time
- Target : Class (0 = légitime, 1 = fraude)

---

## Installation

```bash
pip install -r requirements.txt
```

## Lancement de la WebApp

```bash
streamlit run app.py
```

---

## Stack technique

- Python 3.10+
- scikit-learn, pandas, numpy, matplotlib, seaborn
- kagglehub (téléchargement dataset)
- streamlit (webapp de prédiction)