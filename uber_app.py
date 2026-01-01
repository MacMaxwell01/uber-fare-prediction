# uber_app.py
import streamlit as st
import pandas as pd
import joblib
<<<<<<< HEAD
=======
from datetime import datetime
>>>>>>> 5c220137aebbf40d81dfc03c386c4e690cc7d586

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

<<<<<<< HEAD
# Pickup hour slider (0-23)
pickup_hour = st.slider("Pickup Hour (0-23)", 0, 23, 14)

# Pickup day dropdown
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
pickup_day = st.selectbox("Pickup Day", options=days)
pickup_day_index = days.index(pickup_day)  # Convert to 0-6 for model

# When button clicked
if st.button("Predict Fare"):
    try:
=======

        # Create DataFrame with all features
        input_data = pd.DataFrame({
            'pickup_longitude': [pickup_longitude],
            'pickup_latitude': [pickup_latitude],
            'dropoff_longitude': [dropoff_longitude],
            'dropoff_latitude': [dropoff_latitude],
            'passenger_count': [passenger_count],
            'pickup_hour': [pickup_hour],
<<<<<<< HEAD
            'pickup_day': [pickup_day_index]
=======

        # Make prediction
        fare_prediction = model.predict(input_data)
        st.success(f"Predicted Fare: ${fare_prediction[0]:.2f}")

    except Exception as e:
        st.error(f"Error: {e}")
