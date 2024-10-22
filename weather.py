import requests
from datetime import datetime

API_KEY = 'Your Key here....obtain freely by signup on openWeather'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def fetch_weather_data(city_name):
    """Fetch weather data for a given city."""
    request_url = f'{BASE_URL}?q={city_name}&appid={API_KEY}&units=metric'
    response = requests.get(request_url)
    return response.json()

def extract_weather_info(data):
    """Extract relevant weather information from the API response."""
    if 'main' not in data or 'weather' not in data:
        return None  # Handle cases where data is not found

    weather_info = {
        'city': data.get('name'),
        'longitude': data['coord']['lon'],
        'latitude': data['coord']['lat'],
        'weather_id': data['weather'][0]['id'],
        'weather_main': data['weather'][0]['main'],
        'weather_description': data['weather'][0]['description'],
        'temperature': data['main']['temp'],
        'feels_like': data['main']['feels_like'],
        'temp_min': data['main']['temp_min'],
        'temp_max': data['main']['temp_max'],
        'pressure': data['main']['pressure'],
        'humidity': data['main']['humidity'],
        'visibility': data.get('visibility', 'N/A'),
        'wind_speed': data['wind'].get('speed', 'N/A'),
        'wind_direction': data['wind'].get('deg', 'N/A'),
        'wind_gust': data['wind'].get('gust', 'N/A'),
        'date_time': datetime.fromtimestamp(data['dt']).strftime('%Y-%m-%d %H:%M:%S'),
        'country': data['sys']['country'],
        'sunrise': datetime.fromtimestamp(data['sys']['sunrise']).strftime('%Y-%m-%d %H:%M:%S'),
        'sunset': datetime.fromtimestamp(data['sys']['sunset']).strftime('%Y-%m-%d %H:%M:%S'),
    }
    return weather_info
