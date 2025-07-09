import os
print("Current working directory:", os.getcwd())
print("Files in current directory:", os.listdir())

import streamlit as st
import pandas as pd
import pickle

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Telco Churn Prediction")

gender = st.selectbox("Gender", ["Male", "Female"])
senior = st.selectbox("Senior Citizen", [0, 1])
tenure = st.slider("Tenure (months)", 0, 72)
monthly_charges = st.number_input("Monthly Charges", 0.0, 200.0)

input_data = pd.DataFrame({
    "gender": [gender],
    "SeniorCitizen": [senior],
    "tenure": [tenure],
    "MonthlyCharges": [monthly_charges]
})

if st.button("Predict"):
    prediction = model.predict(input_data)
    st.write("Prediction:", "Churn" if prediction[0] == 1 else "No Churn")
