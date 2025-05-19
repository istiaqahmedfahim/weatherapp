import streamlit as st
import requests

st.title("🌦️ Weather App (Using REST API)")

API_URL = "http://127.0.0.1:8000"

# Form to Get Weather Info
city = st.text_input("Enter city name:")

if st.button("Get Weather"):
    response = requests.get(f"{API_URL}/weather/{city}")
    if response.status_code == 200:
        data = response.json()
        if "error" in data:
            st.error(data["error"])
        else:
            st.success(f"Weather in {city.title()}:")
            st.write(f"🌡️ Temperature: {data['temperature']}°C")
            st.write(f"☁️ Condition: {data['description'].capitalize()}")
    else:
        st.error("Failed to connect to API.")

# Form to Add New Weather Info
st.subheader("Add New Weather Info")

new_city = st.text_input("City:")
temp = st.number_input("Temperature (°C)", step=1)
desc = st.text_input("Weather Description")

if st.button("Add Weather Info"):
    payload = {
        "temperature": temp,
        "description": desc
    }
    response = requests.post(f"{API_URL}/weather/{new_city}", json=payload)
    if response.status_code == 200:
        st.success(response.json()["message"])
    else:
        st.error("Failed to add weather data.")
