import pandas as pd
import numpy as np
import joblib

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB

from sklearn.metrics import accuracy_score

train = pd.read_csv("data/training.csv")
test = pd.read_csv("data/testing.csv")

print(train.head())

X_train = train.drop("prognosis", axis=1)
y_train = train["prognosis"]

X_test = test.drop("prognosis", axis=1)
y_test = test["prognosis"]

dt = DecisionTreeClassifier(random_state=42)

dt.fit(X_train, y_train)

dt_pred = dt.predict(X_test)

print("Decision Tree Accuracy:",
      accuracy_score(y_test, dt_pred))

rf = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

rf.fit(X_train, y_train)

rf_pred = rf.predict(X_test)

print("Random Forest Accuracy:",
      accuracy_score(y_test, rf_pred))

nb = GaussianNB()

nb.fit(X_train, y_train)

nb_pred = nb.predict(X_test)

print("Naive Bayes Accuracy:",
      accuracy_score(y_test, nb_pred))

print("\nModel Accuracy")

print("----------------------")

print("Decision Tree :", accuracy_score(y_test, dt_pred))

print("Random Forest :", accuracy_score(y_test, rf_pred))

print("Naive Bayes   :", accuracy_score(y_test, nb_pred))

joblib.dump(dt, "models/decision_tree.pkl")
joblib.dump(rf, "models/random_forest.pkl")
joblib.dump(nb, "models/naive_bayes.pkl")

import pandas as pd
import joblib

model = joblib.load("models/random_forest.pkl")

data = pd.read_csv("data/training.csv")

symptoms = list(data.columns[:-1])

user_input = []

for symptom in symptoms:

    value = int(input(f"{symptom} (0 or 1): "))

    user_input.append(value)

prediction = model.predict([user_input])

print("\nPredicted Disease:")

print(prediction[0])

import streamlit as st
import pandas as pd
import joblib

model = joblib.load("models/random_forest.pkl")

train = pd.read_csv("data/training.csv")

symptoms = train.columns[:-1]

st.title("Disease Prediction System")

st.write("Select Symptoms")

user_input = []

for symptom in symptoms:

    value = st.selectbox(symptom, [0,1])

    user_input.append(value)

if st.button("Predict"):

    prediction = model.predict([user_input])

    st.success(f"Predicted Disease : {prediction[0]}")
