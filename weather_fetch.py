import requests
import pandas as pd

API_KEY = "60eac4f52fdf4db7877125836251403"  # Replace with your Weather API key
BASE_URL = "https://api.weatherapi.com/v1/current.json"

def fetch_weather(city):
    """Fetches weather details for a given city."""
    response = requests.get(BASE_URL, params={"key": API_KEY, "q": city})
    
    if response.status_code == 200:
        data = response.json()
        return {
            "City": data["location"]["name"],
            "Temperature (°C)": data["current"]["temp_c"],
            "Humidity (%)": data["current"]["humidity"],
            "Wind Speed (km/h)": data["current"]["wind_kph"],
            "Condition": data["current"]["condition"]["text"]
        }
    else:
        print(f"Failed to fetch data for {city}")
        return None

def save_to_csv(weather_data, filename="weather_data.csv"):
    """Saves weather data to a CSV file."""
    df = pd.DataFrame(weather_data)
    df.to_csv(filename, index=False)
    print(f"✅ Data saved to {filename}")

def main():
    cities = input("Enter city names (comma-separated): ").split(",")
    cities = [city.strip() for city in cities]  # Remove extra spaces

    weather_list = []
    
    for city in cities:
        weather = fetch_weather(city)
        if weather:
            weather_list.append(weather)

    if weather_list:
        save_to_csv(weather_list)

if __name__ == "__main__":
    main()






