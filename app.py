import streamlit as st

st.experimental_memo.clear()
st.experimental_singleton.clear()

import os
print("Current working directory:", os.getcwd())
print("Files in current directory:", os.listdir())

import streamlit as st
import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Telco Churn Prediction")

# Collect inputs
gender = st.selectbox("Gender", ["Male", "Female"])
senior = st.selectbox("Senior Citizen", [0, 1])
tenure = st.slider("Tenure (months)", 0, 72)
monthly_charges = st.number_input("Monthly Charges", 0.0, 200.0)

# Simple encoding for gender
gender_encoded = 1 if gender == "Male" else 0

# Build input DataFrame
input_data = pd.DataFrame({
    "gender": [gender_encoded],
    "SeniorCitizen": [senior],
    "tenure": [tenure],
    "MonthlyCharges": [monthly_charges]
})

# Apply scaling if your model was trained on scaled data
scaler = StandardScaler()
# Fit scaler to one example row (dummy training)
scaler.fit([[0, 0, 0, 0]])  # this won't change values but avoids error
input_scaled = scaler.transform(input_data)

# Predict
if st.button("Predict"):
    try:
        prediction = model.predict(input_scaled)
        st.write("Prediction:", "Churn" if prediction[0] == 1 else "No Churn")
    except Exception as e:
        st.error(f"Prediction error: {e}")
