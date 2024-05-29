from flask import Flask, render_template
import requests
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def weather():
    try:
        response = requests.get('https://vm.nathoro.ru/weather?lattitude=54.32&longitude=48.38')
        response.raise_for_status()
        weather_data = response.json()

        # Convert date strings to datetime objects
        for weather in weather_data:
            weather['date'] = datetime.fromisoformat(weather['date'])
            weather['temperature'] = round(weather['temperature'], 1)  # округление температуры до 1 знака после запятой
            weather['windSpeed'] = round(weather['windSpeed'], 1)      # округление скорости ветра до 1 знака после запятой
            weather['humidity'] = round(weather['humidity'], 1)        # округление влажности до 1 знака после запятой
    except requests.exceptions.RequestException as e:
        weather_data = []
        print(f"Error fetching weather data: {e}")

    return render_template('weather.html', weather_data=weather_data)

if __name__ == '__main__':
    app.run(debug=True)
