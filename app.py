import streamlit as st
import pandas as pd
import pickle

# Show current files (for debugging in Streamlit UI)
import os
st.write("Current working directory:", os.getcwd())
st.write("Files here:", os.listdir())

from sklearn.preprocessing import StandardScaler

# Load your pre-trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Telco Churn Prediction")

# Collect user input
gender = st.selectbox("Gender", ["Male", "Female"])
senior = st.selectbox("Senior Citizen", [0, 1])
tenure = st.slider("Tenure (months)", 0, 72)
monthly_charges = st.number_input("Monthly Charges", 0.0, 200.0)

# Encode gender
gender_encoded = 1 if gender == "Male" else 0

# Build input DataFrame matching training features order and names
input_data = pd.DataFrame({
    "gender": [gender_encoded],
    "SeniorCitizen": [senior],
    "tenure": [tenure],
    "MonthlyCharges": [monthly_charges]
})

if st.button("Predict"):
    try:
        prediction = model.predict(input_scaled)
        st.write("Prediction:", "Churn" if prediction[0] == 1 else "No Churn")
    except Exception as e:
        st.error(f"Prediction error: {e}")
