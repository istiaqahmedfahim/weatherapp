from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Sample database
weather_db = {
    "Dhaka": {"temperature": 30, "description": "hot and humid"},
    "London": {"temperature": 18, "description": "cloudy"},
}

# Define request body model
class WeatherInfo(BaseModel):
    temperature: int
    description: str

@app.get("/")
def read_root():
    return {"message": "Welcome to the Weather API!"}

@app.get("/weather/{city}")
def get_weather(city: str):
    city = city.title()
    if city in weather_db:
        return weather_db[city]
    return {"error": "City not found"}

@app.post("/weather/{city}")
def add_weather(city: str, info: WeatherInfo):
    city = city.title()
    weather_db[city] = info.dict()
    return {"message": f"Weather for {city} added successfully"}
