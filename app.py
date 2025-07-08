import streamlit as st
import pickle
import numpy as np

# Load model and scaler
with open('churn_model.pkl', 'rb') as f:
    model = pickle.load(f)

with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

# Set up the UI
st.set_page_config(page_title="Customer Churn Prediction App")
st.title("📉 Customer Churn Prediction")
st.markdown("Use the form below to predict if a customer is likely to churn.")

# Input fields
gender = st.selectbox("Gender", ["Female", "Male"])
senior_citizen = st.selectbox("Senior Citizen", ["No", "Yes"])
partner = st.selectbox("Has Partner?", ["No", "Yes"])
dependents = st.selectbox("Has Dependents?", ["No", "Yes"])
tenure = st.slider("Tenure (Months)", 0, 72, 12)
monthly_charges = st.number_input("Monthly Charges", min_value=0.0, value=70.0)
total_charges = st.number_input("Total Charges", min_value=0.0, value=1500.0)

phone_service = st.selectbox("Phone Service", ["No", "Yes"])
multiple_lines = st.selectbox("Multiple Lines", ["No", "No phone service", "Yes"])
internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
online_security = st.selectbox("Online Security", ["No", "Yes", "No internet service"])
online_backup = st.selectbox("Online Backup", ["No", "Yes", "No internet service"])
device_protection = st.selectbox("Device Protection", ["No", "Yes", "No internet service"])
tech_support = st.selectbox("Tech Support", ["No", "Yes", "No internet service"])
streaming_tv = st.selectbox("Streaming TV", ["No", "Yes", "No internet service"])
streaming_movies = st.selectbox("Streaming Movies", ["No", "Yes", "No internet service"])

contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
paperless_billing = st.selectbox("Paperless Billing", ["No", "Yes"])
payment_method = st.selectbox("Payment Method", [
    "Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"
])

# Label Encoding mapping based on training
yesno = {"No": 0, "Yes": 1}
gender_map = {"Female": 0, "Male": 1}
multiple_lines_map = {"No": 0, "No phone service": 1, "Yes": 2}
internet_service_map = {"DSL": 0, "Fiber optic": 1, "No": 2}
online_map = {"No": 0, "Yes": 1, "No internet service": 2}
contract_map = {"Month-to-month": 0, "One year": 1, "Two year": 2}
payment_map = {
    "Electronic check": 0,
    "Mailed check": 1,
    "Bank transfer (automatic)": 2,
    "Credit card (automatic)": 3
}

# Create feature array in correct order
input_data = np.array([[
    gender_map[gender],
    yesno[senior_citizen],
    yesno[partner],
    yesno[dependents],
    tenure,
    monthly_charges,
    total_charges,
    yesno[phone_service],
    multiple_lines_map[multiple_lines],
    internet_service_map[internet_service],
    online_map[online_security],
    online_map[online_backup],
    online_map[device_protection],
    online_map[tech_support],
    online_map[streaming_tv],
    online_map[streaming_movies],
    contract_map[contract],
    yesno[paperless_billing],
    payment_map[payment_method]
]])

# Scale input
input_scaled = scaler.transform(input_data)

# Predict
if st.button("Predict Churn"):
    prediction = model.predict(input_scaled)[0]
    probability = model.predict_proba(input_scaled)[0][1] * 100

    if prediction == 1:
        st.error(f"⚠️ The customer is likely to **CHURN** with a probability of {probability:.2f}%.")
    else:
        st.success(f"✅ The customer is likely to **STAY** with a probability of {100 - probability:.2f}%.")
