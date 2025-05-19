import streamlit as st
import requests

# Title of the app
st.title("🌦️ Simple Weather App")

# User input
city = st.text_input("Enter city name:")

# Button to trigger API call
if st.button("Get Weather"):
    if city:
        # Replace this with your OpenWeatherMap API key
        API_KEY = "91693b637b61ecc201908a21156af97a"
        URL = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

        # Request to the API
        response = requests.get(URL)
        data = response.json()

        if response.status_code == 200:
            temperature = data["main"]["temp"]
            description = data["weather"][0]["description"]
            st.success(f"Weather in {city.title()}")
            st.write(f"🌡️ Temperature: **{temperature}°C**")
            st.write(f"☁️ Condition: **{description.capitalize()}**")
        else:
            st.error(f"City not found: {data['message']}")
    else:
        st.warning("Please enter a city name.")