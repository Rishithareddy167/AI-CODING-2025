import requests
import json

def get_weather(city_name, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    complete_url = f"{base_url}?q={city_name}&appid={api_key}&units=metric"

    try:
        # Try to connect to the API
        response = requests.get(complete_url, timeout=5)
        response.raise_for_status()  # Raise error for bad responses (4xx, 5xx)

        # Convert response to JSON
        weather_data = response.json()

        # Display formatted JSON output in terminal
        print(json.dumps(weather_data, indent=4))

        # ---------- Create and save JSON file ----------
        file_name = f"weather_{city_name}.json"
        with open(file_name, "w") as file:
            json.dump(weather_data, file, indent=4)

        print(f"\n✅ Weather data saved to '{file_name}'")

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
