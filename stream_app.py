import streamlit as st
import pandas as pd
import joblib

# Load your pre-trained model
model = joblib.load("med_charges_random_forest_model.pkl")

# Title of the app
st.title("Medical Charges Prediction App")

# Input fields for user data
age = st.number_input("Age", min_value=18, max_value=64, value=25)
sex = st.selectbox("Sex", ["female", "male"])
bmi = st.number_input("BMI", min_value=15.0, max_value=54.0, value=25.0)
children = st.number_input("Children", min_value=0, max_value=5, value=0)
smoker = st.selectbox("Smoker", ["no", "yes"])
region = st.selectbox("Region", ["northeast", "northwest", "southeast", "southwest"])

# One-hot encoding the categorical data
sex_dict = {"female": [1, 0], "male": [0, 1]}  # For 'sex_male' and 'sex_female'
smoker_dict = {"no": [1, 0], "yes": [0, 1]}   # For 'smoker_yes' and 'smoker_no'
region_dict = {
    "northeast": [1, 0, 0, 0],
    "northwest": [0, 1, 0, 0],
    "southeast": [0, 0, 1, 0],
    "southwest": [0, 0, 0, 1]
}

# Creating the input data for prediction
input_data = {
    'age': age,
    'bmi': bmi,
    'children': children,
    # Unpack the lists from the dictionaries
    'sex_female': sex_dict[sex][0],
    'sex_male': sex_dict[sex][1],
    'smoker_no': smoker_dict[smoker][0],
    'smoker_yes': smoker_dict[smoker][1],
    # One-hot encoded region
    'region_northeast': region_dict[region][0],
    'region_northwest': region_dict[region][1],
    'region_southeast': region_dict[region][2],
    'region_southwest': region_dict[region][3]
}

# Convert the input data into a DataFrame
input_df = pd.DataFrame([input_data])

# Predict button
if st.button("Predict Medical Charges"):
    prediction = model.predict(input_df)
    st.write(f"Predicted Medical Charges: ${prediction[0]:,.2f}")
