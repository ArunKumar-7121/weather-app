from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace with your API key from OpenWeatherMap
WEATHER_API_KEY = "bd5e378503939ddaee76f12ad7a97608"
WEATHER_BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.route('/current-weather', methods=['GET'])
def current_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({"error": "Please provide a city"}), 400

    # Fetch weather data from OpenWeatherMap
    response = requests.get(WEATHER_BASE_URL, params={
        'q': city,
        'appid': WEATHER_API_KEY,
        'units': 'metric'
    })
    if response.status_code != 200:
        return jsonify({"error": "Failed to fetch weather data"}), response.status_code

    data = response.json()
    weather = {
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "description": data["weather"][0]["description"],
    }
    return jsonify(weather)

if __name__ == '__main__':
    app.run(debug=True)
