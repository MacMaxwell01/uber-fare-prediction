import streamlit as st
import joblib
import pandas as pd

# Load the saved model
model = joblib.load("uber_fare_model.pkl")

# Streamlit app layout
st.title("Uber Fare Prediction App")

# Input fields
pickup_longitude = st.number_input("Pickup Longitude")
pickup_latitude = st.number_input("Pickup Latitude")
dropoff_longitude = st.number_input("Dropoff Longitude")
dropoff_latitude = st.number_input("Dropoff Latitude")
passenger_count = st.number_input("Passenger Count", min_value=1, step=1)

# Collect inputs in a DataFrame
input_data = pd.DataFrame({
    "pickup_longitude": [pickup_longitude],
    "pickup_latitude": [pickup_latitude],
    "dropoff_longitude": [dropoff_longitude],
    "dropoff_latitude": [dropoff_latitude],
    "passenger_count": [passenger_count]
})

# Predict fare
if st.button("Predict Fare"):
    fare_prediction = model.predict(input_data)
    st.success(f"Predicted Fare: ${fare_prediction[0]:.2f}")
