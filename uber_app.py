# uber_app.py
import streamlit as st
import pandas as pd
import joblib
from datetime import datetime

# Load the trained model
model = joblib.load("uber_fare_model.pkl")

st.title("Uber Fare Prediction App 🚖")
st.header("Enter trip details:")

# User inputs
pickup_longitude = st.number_input("Pickup Longitude", value=-73.985428, format="%.6f")
pickup_latitude = st.number_input("Pickup Latitude", value=40.748817, format="%.6f")
dropoff_longitude = st.number_input("Dropoff Longitude", value=-73.985135, format="%.6f")
dropoff_latitude = st.number_input("Dropoff Latitude", value=40.758896, format="%.6f")
passenger_count = st.number_input("Number of Passengers", min_value=1, max_value=10, value=1)

# Let user input datetime instead of hour/day separately
pickup_datetime = st.text_input("Pickup datetime (YYYY-MM-DD HH:MM:SS)", "2026-01-01 14:00:00")

# When button clicked
if st.button("Predict Fare"):
    try:
        # Convert to datetime
        dt = pd.to_datetime(pickup_datetime)

        # Extract hour and day
        pickup_hour = dt.hour
        pickup_day = dt.weekday()  # Monday=0, Sunday=6

        # Create DataFrame with all features
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
        st.success(f"Predicted Fare: ${fare_prediction[0]:.2f}")

    except Exception as e:
        st.error(f"Error: {e}")
