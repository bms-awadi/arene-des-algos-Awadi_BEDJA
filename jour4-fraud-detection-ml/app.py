import streamlit as st
import joblib
import numpy as np
import pandas as pd

@st.cache_resource
def charger_modele():
    artefact = joblib.load("modele.joblib")
    return artefact["modele"], artefact["scaler"]

@st.cache_data
def charger_dataset():
    df = pd.read_csv("data/creditcard.csv")
    return df

modele, scaler = charger_modele()
df = charger_dataset()

FEATURE_NAMES = [f"V{i}" for i in range(1, 29)] + ["Amount", "Time"]

st.title("Détection de fraude bancaire")

mode = st.radio("Mode de sélection", [
    "Index manuel",
    "Aléatoire",
    "Aléatoire parmi les fraudes",
    "Importer un CSV"
])

def predire(transaction):
    features = transaction[FEATURE_NAMES].values.reshape(1, -1)
    if any(abs(v) > 50 for v in features[0]):
        st.warning("Certaines valeurs sont hors de la plage habituelle.")
    features_scaled = scaler.transform(features)
    prediction = int(modele.predict(features_scaled)[0])
    proba = float(modele.predict_proba(features_scaled)[0][1])
    return prediction, proba

def afficher_resultat(prediction, proba, vraie_classe=None):
    st.divider()
    if prediction == 1:
        st.error(f"Prédiction : FRAUDE (probabilité {proba*100:.1f}%)")
    else:
        st.success(f"Prédiction : Transaction légitime (probabilité fraude : {proba*100:.1f}%)")
    st.progress(proba, text=f"Score de risque : {proba*100:.1f}%")
    if vraie_classe is not None:
        if prediction == vraie_classe:
            st.caption("Prédiction correcte")
        else:
            st.caption("Prédiction incorrecte")

# --- Modes dataset interne ---
if mode in ["Index manuel", "Aléatoire", "Aléatoire parmi les fraudes"]:

    if mode == "Index manuel":
        idx = st.number_input("Index de la transaction", min_value=0,
                              max_value=len(df) - 1, value=0, step=1)
        transaction = df.iloc[int(idx)]

    elif mode == "Aléatoire":
        if st.button("Tirer une transaction au hasard"):
            st.session_state["idx"] = np.random.randint(0, len(df))
        transaction = df.iloc[st.session_state.get("idx", 0)]

    else:
        fraudes = df[df["Class"] == 1]
        if st.button("Tirer une fraude au hasard"):
            st.session_state["idx_fraude"] = np.random.randint(0, len(fraudes))
        transaction = fraudes.iloc[st.session_state.get("idx_fraude", 0)]

    vraie_classe = int(transaction["Class"])
    st.info(f"Vraie classe : {'FRAUDE' if vraie_classe == 1 else 'Légitime'} "
            f"| Amount : {transaction['Amount']:.2f}€")

    prediction, proba = predire(transaction)
    afficher_resultat(prediction, proba, vraie_classe)

# --- Mode import CSV ---
else:
    st.markdown("Importez un CSV avec les colonnes V1-V28, Amount, Time. "
                "La colonne `Class` est optionnelle. Une ou plusieurs lignes acceptées.")

    fichier = st.file_uploader("Choisir un fichier CSV", type=["csv"])

    if fichier is not None:
        try:
            df_import = pd.read_csv(fichier)

            # Vérification des colonnes
            cols_manquantes = [c for c in FEATURE_NAMES if c not in df_import.columns]
            if cols_manquantes:
                st.error(f"Colonnes manquantes : {cols_manquantes}")
            else:
                has_class = "Class" in df_import.columns
                st.success(f"{len(df_import)} transaction(s) chargée(s).")

                resultats = []
                for i, row in df_import.iterrows():
                    prediction, proba = predire(row)
                    label = "FRAUDE" if prediction == 1 else "Légitime"
                    res = {
                        "Transaction": i,
                        "Prédiction": label,
                        "Probabilité fraude": f"{proba*100:.1f}%"
                    }
                    if has_class:
                        vraie = int(row["Class"])
                        res["Vraie classe"] = "FRAUDE" if vraie == 1 else "Légitime"
                        res["Correct"] = "Yes" if prediction == vraie else "False"
                    resultats.append(res)

                df_resultats = pd.DataFrame(resultats)
                st.dataframe(df_resultats, use_container_width=True)

                # Téléchargement des résultats
                csv_out = df_resultats.to_csv(index=False).encode("utf-8")
                st.download_button(
                    label="Télécharger les résultats",
                    data=csv_out,
                    file_name="resultats_predictions.csv",
                    mime="text/csv"
                )

        except Exception as e:
            st.error(f"Erreur lors de la lecture du fichier : {e}")