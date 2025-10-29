import requests

def get_weather(city_name, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    complete_url = f"{base_url}?q={city_name}&appid={api_key}&units=metric"

    try:
        response = requests.get(complete_url, timeout=5)
        response.raise_for_status()  # Raises error for 4xx/5xx status codes

        data = response.json()

        # Check if the API returned a valid city
        if data.get("cod") != 200:
            print("Error: City not found. Please enter a valid city.")
            return

        # Extract specific weather details
        city = data["name"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]

        # Display in user-friendly format
        print(f"\nCity: {city}")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {description.capitalize()}")

    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to API. Check your internet connection.")
    except requests.exceptions.Timeout:
        print("Error: The request timed out. Try again later.")
    except requests.exceptions.RequestException:
        print("Error: Could not connect to API. Check your API key or network connection.")


# Example usage
if __name__ == "__main__":
    api_key = input("Enter your OpenWeatherMap API key: ")
    city = input("Enter city name: ")
    get_weather(city, api_key)
