import csv
import os


def read_cities_from_file(filename='cities.txt'):
    """Read city names from a text file."""
    with open(filename, 'r') as file:
        return [line.strip() for line in file.readlines()]


def save_to_csv(weather_data, filename='weather_data.csv'):
    """Save weather data to a CSV file, appending if it exists."""
    file_exists = os.path.isfile(filename)

    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=weather_data[0].keys())

        # Write header only if the file does not exist
        if not file_exists:
            writer.writeheader()

        writer.writerows(weather_data)
