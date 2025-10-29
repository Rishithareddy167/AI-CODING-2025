import requests
import json
import os

def get_weather(city_name, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    complete_url = f"{base_url}?q={city_name}&appid={api_key}&units=metric"

    try:
        # Send API request
        response = requests.get(complete_url, timeout=5)
        response.raise_for_status()

        data = response.json()

        # Check if the city is valid
        if data.get("cod") != 200:
            print("Error: City not found. Please enter a valid city.")
            return

        # Extract important details
        city = data["name"]
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]

        # Display formatted result in console
        print(f"\nCity: {city}")
        print(f"Temperature: {temp}°C")
        print(f"Humidity: {humidity}%")
        print(f"Weather: {description.capitalize()}")

        # Prepare data to store
        new_entry = {
            "city": city,
            "temp": temp,
            "humidity": humidity,
            "weather": description.capitalize()
        }

        # ---------- Append to results.json ----------
        file_path = "results.json"

        # If file exists, load old data
        if os.path.exists(file_path):
            with open(file_path, "r") as file:
                try:
                    all_data = json.load(file)
                except json.JSONDecodeError:
                    all_data = []  # empty if corrupt or empty file
        else:
            all_data = []

        # Add new entry
        all_data.append(new_entry)

        # Write updated list back to file
        with open(file_path, "w") as file:
            json.dump(all_data, file, indent=4)

        print(f"\n✅ Weather data for {city} saved to '{file_path}'")

    # ------------------- Error Handling -------------------
    except requests.exceptions.ConnectionError:
        print("Error: Could not connect to API. Check your internet connection.")
    except requests.exceptions.Timeout:
        print("Error: The request timed out. Try again later.")
    except requests.exceptions.RequestException:
        print("Error: Could not connect to API. Check your API key or network connection.")

# ------------------- Example Usage -------------------
if __name__ == "__main__":
    api_key = input("Enter your OpenWeatherMap API key: ")
    city = input("Enter city name: ")
    get_weather(city, api_key)
