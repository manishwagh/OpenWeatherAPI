from weather import fetch_weather_data, extract_weather_info
from file_handler import read_cities_from_file, save_to_csv


def main():
    weather_data = []

    cities = read_cities_from_file()

    for city in cities:
        data = fetch_weather_data(city)
        weather_info = extract_weather_info(data)
        if weather_info:
            weather_data.append(weather_info)
        else:
            print(f"Weather data not found for city: {city}")

    save_to_csv(weather_data)


if __name__ == "__main__":
    main()
