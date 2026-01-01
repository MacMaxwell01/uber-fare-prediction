import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load("uber_fare_model.pkl")

# Input fields
pickup_datetime = st.text_input("Pickup datetime (YYYY-MM-DD HH:MM:SS)")
pickup_longitude = st.number_input("Pickup longitude")
pickup_latitude = st.number_input("Pickup latitude")
dropoff_longitude = st.number_input("Dropoff longitude")
dropoff_latitude = st.number_input("Dropoff latitude")
passenger_count = st.number_input("Passenger count", min_value=1, step=1)

if st.button("Predict Fare"):
    try:
        # Convert datetime to datetime object
        pickup_dt = pd.to_datetime(pickup_datetime)
        
        # Extract hour and day
        pickup_hour = pickup_dt.hour
        pickup_day = pickup_dt.dayofweek
        
        # Prepare input data with the same features as training
        input_data = pd.DataFrame([{
            "pickup_longitude": pickup_longitude,
            "pickup_latitude": pickup_latitude,
            "dropoff_longitude": dropoff_longitude,
            "dropoff_latitude": dropoff_latitude,
            "passenger_count": passenger_count,
            "pickup_hour": pickup_hour,
            "pickup_day": pickup_day
        }])
        
        # Predict
        fare_prediction = model.predict(input_data)
        st.success(f"Predicted Fare: ${fare_prediction[0]:.2f}")
        
    except Exception as e:
        st.error(f"Error: {e}")
