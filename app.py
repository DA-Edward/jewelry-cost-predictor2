
import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("jewelry_cost_model.pkl")

st.title("💎 Jewelry Cost Predictor")

st.markdown("Enter the details below to estimate manufacturing cost:")

gold_type = st.selectbox("Gold Type", ["18KW", "18KR", "18KY", "PT950"])
gold_weight = st.number_input("Gold Weight (gm)", min_value=0.0, value=2.8)
gold_cost = st.number_input("Gold Cost (USD)", min_value=0.0, value=315.0)
accent_carat = st.number_input("Accent Stone Carat", min_value=0.0, value=0.18)
accent_price = st.number_input("Accent Stone Price (USD)", min_value=0.0, value=54.0)
labor = st.number_input("Labor Cost (USD)", min_value=0.0, value=145.0)
mould = st.number_input("Mould Fee (USD)", min_value=0.0, value=0.0)
main_carat = st.number_input("Main Stone Carat", min_value=0.0, value=1.0)

if st.button("Predict Cost"):
    df = pd.DataFrame([{
        "GoldType": gold_type,
        "GoldWeight": gold_weight,
        "GoldCost": gold_cost,
        "AccentStones_Carat": accent_carat,
        "AccentStones_Price": accent_price,
        "LaborCost": labor,
        "MouldFee": mould,
        "MainStone_Carat": main_carat
    }])
    prediction = model.predict(df)[0]
    st.success(f"💰 Estimated Manufacturing Cost: **${prediction:.2f}**")
