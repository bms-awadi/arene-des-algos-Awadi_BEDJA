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
| **2** | Bootstrap OOB, stabilité modèle accuracy trompeuse confirmée sur dataset déséquilibré |
| **3** | Validation croisée k-fold, LOO impossible sur déséquilibre, StratifiedKFold vs standard |

---

## Dataset

Source : [Kaggle : Credit Card Fraud Detection](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud)  
Téléchargement via `kagglehub`.

---

## Installation

```bash
pip install -r requirements.txt
```
---

## Stack technique

- Python 3.10+
- scikit-learn, pandas, numpy, matplotlib, seaborn
- kagglehub (téléchargement dataset)