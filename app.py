import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("models/random_forest.pkl")

# Load dataset
data = pd.read_csv("data/training.csv")

# Get symptom names
symptoms = list(data.columns[:-1])

st.set_page_config(
    page_title="Disease Prediction System",
    page_icon="🩺",
    layout="wide"
)

st.title("🩺 Intelligent Disease Prediction System")

st.write("### Select your symptoms")

selected = st.multiselect(
    "Symptoms",
    symptoms
)

if st.button("Predict Disease"):

    user_input = [0] * len(symptoms)

    for symptom in selected:
        index = symptoms.index(symptom)
        user_input[index] = 1

    prediction = model.predict([user_input])

    st.success(f"Predicted Disease: **{prediction[0]}**")