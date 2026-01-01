# uber_app.py
import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("uber_fare_model.pkl")  # Make sure your .pkl file is in the same folder

st.title("Uber Fare Prediction App 🚖")

st.header("Enter trip details:")

# User inputs
pickup_longitude = st.number_input("Pickup Longitude", value=-73.985428, format="%.6f")
pickup_latitude = st.number_input("Pickup Latitude", value=40.748817, format="%.6f")
dropoff_longitude = st.number_input("Dropoff Longitude", value=-73.985135, format="%.6f")
dropoff_latitude = st.number_input("Dropoff Latitude", value=40.758896, format="%.6f")
passenger_count = st.number_input("Number of Passengers", min_value=1, max_value=10, value=1)

pickup_hour = st.number_input("Pickup Hour (0-23)", min_value=0, max_value=23, value=14)
pickup_day = st.number_input("Pickup Day (0=Monday, 6=Sunday)", min_value=0, max_value=6, value=2)

# Predict fare when button is clicked
if st.button("Predict Fare"):
    # Create a DataFrame with the input values
    input_data = pd.DataFrame({
        'pickup_longitude': [pickup_longitude],
        'pickup_latitude': [pickup_latitude],
        'dropoff_longitude': [dropoff_longitude],
        'dropoff_latitude': [dropoff_latitude],
        'passenger_count': [passenger_count],
        'pickup_hour': [pickup_hour],
        'pickup_day': [pickup_day]
    })

    # Make prediction
    fare_prediction = model.predict(input_data)
    
    # Show the result
    st.success(f"Predicted Fare: ${fare_prediction[0]:.2f}")
