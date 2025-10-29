import requests
import json

def get_weather(city_name, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    complete_url = f"{base_url}?q={city_name}&appid={api_key}&units=metric"

    try:
        # Connect to the API
        response = requests.get(complete_url, timeout=5)
        response.raise_for_status()

        # Convert response to JSON
        weather_data = response.json()

        # -------- Extract specific fields --------
        city = weather_data["name"]
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        description = weather_data["weather"][0]["description"]

        # -------- Display in user-friendly format --------
        print(f"\nCity: {city}")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {description.capitalize()}")

        # Save entire response as JSON (optional)
        with open(f"weather_{city}.json", "w") as file:
            json.dump(weather_data, file, indent=4)

    except requests.exceptions.HTTPError:
        print("Error: Invalid response from the API. Please check your API key or city name.")
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to API. Check your internet connection.")
    except requests.exceptions.Timeout:
        print("Error: The request timed out. Try again later.")
    except requests.exceptions.RequestException:
        print("Error: Could not connect to API. Check your API key or network connection.")

if __name__ == "__main__":
    api_key = input("Enter your OpenWeatherMap API key: ")
    city = input("Enter city name: ")
    get_weather(city, api_key)
