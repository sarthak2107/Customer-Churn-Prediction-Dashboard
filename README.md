# 📉 Customer Churn Prediction Dashboard

## 📊 Project Overview

An interactive and intelligent dashboard to predict customer churn for telecom services using machine learning. Built using **Python**, **Streamlit**, and **XGBoost**, this project enables stakeholders to identify potential churners and take proactive actions to improve customer retention.

---

## 🎯 Objectives

- Predict whether a customer will churn or stay based on behavioral and service features.
- Provide real-time churn probability through an interactive form.
- Visualize patterns in customer churn across services, contracts, and payments.
- Support decision-makers with insights into key churn-driving factors.

---

## 🧠 Machine Learning Model

- **Model Type:** XGBoost Classifier  
- **Dataset:** `customer.csv`  
- **Trained Model:** `churn_model.pkl`  
- **Target Feature:** `Churn` (Yes/No)

---

## 📈 Key Features

- 💡 Real-time **churn prediction** using user-input customer profile.
- 📊 Dynamic charts for:
  - Churn Rate Distribution
  - Monthly Charges Comparison
  - Contract Type Impact on Churn
- 🧮 Filters by Internet Service, Contract Type, and Payment Method.
- 🚦 User-friendly UI for testing various churn scenarios.

---

## 📄 Dashboard Preview

📎 **Click below to view the dashboard output (PDF format):**  
👉 [Customer_Churn_Dashboard_Output.pdf](Customer_Churn_Prediction_App.pdf) <!-- Ensure this filename matches your actual PDF filename in GitHub -->

> The PDF contains screenshots of the actual dashboard, including filters, form inputs, predictions, and visual insights.

---

## 📁 Files Included

- `customer.csv` – Cleaned dataset used for training and visualizations  
- `churn_model.pkl` – Trained XGBoost model  
- `app.py` – Streamlit dashboard app code  
- `Customer_Churn_Prediction_App.pdf` – PDF preview of the final dashboard

---

## ⚙️ Tech Stack

- **Python**
- **Streamlit** – UI for real-time model predictions
- **Pandas & NumPy** – Data processing
- **XGBoost** – ML classification model
- **Scikit-learn** – Preprocessing and evaluation
- **Matplotlib / Seaborn** – For visualizations during EDA

---

## 🚀 How to Run This Project

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/churn-dashboard.git
   cd churn-dashboard
