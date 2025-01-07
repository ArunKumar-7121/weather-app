import requests

API_URL = "http://127.0.0.1:5000/current-weather"

def get_weather(city):
    try:
        response = requests.get(API_URL, params={'city': city})
        if response.status_code == 200:
            weather = response.json()
            print(f"Weather in {weather['city']}:")
            print(f"Temperature: {weather['temperature']}°C")
            print(f"Description: {weather['description']}")
        else:
            print("Error:", response.json().get("error", "Unknown error"))
    except Exception as e:
        print("Error fetching weather:", e)

if __name__ == '__main__':
    city = input("Enter a city: ")
    get_weather(city)
