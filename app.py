import streamlit as st
import pickle
import numpy as np

# --- Page Configuration ---
st.set_page_config(page_title="Salary Predictor", page_icon="💼", layout="centered")

# --- Load Model ---
with open("salary_model.pkl", "rb") as file:
    model = pickle.load(file)

# --- App Title ---
st.markdown("""
# Salary Predictor
*Estimate your expected salary based on experience.*
""")

# --- Input Section ---
st.markdown("### Enter your details:")

experience = st.number_input(
    "Years of Experience",
    min_value=0.0,
    max_value=50.0,
    value=1.0,
    step=0.1,
    format="%.1f"
)

# --- Prediction ---
if st.button("Predict Salary"):
    input_array = np.array([[experience]])
    prediction = model.predict(input_array)[0]
    
    st.markdown("---")
    st.markdown(f"### Estimated Salary: `₹{prediction:,.2f}`")
    st.success("Prediction complete ✅")

# --- Footer ---
st.markdown("""
---
👨‍💻 *Built with Python & Scikit-Learn*  
✨ *Deployed using Streamlit*
""")
