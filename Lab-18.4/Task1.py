import requests
import json

def get_weather(city_name, api_key):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    complete_url = f"{base_url}?q={city_name}&appid={api_key}&units=metric"
    
    response = requests.get(complete_url)
    weather_data = response.json()
    
    # Save the JSON output to a file
    with open("weather_output.json", "w") as json_file:
        json.dump(weather_data, json_file, indent=4)
    
    # Display formatted JSON output
    print(json.dumps(weather_data, indent=4))

if __name__ == "__main__":
    api_key = input("Enter your OpenWeatherMap API key: ")
    city = input("Enter city name: ")
    get_weather(city, api_key)
