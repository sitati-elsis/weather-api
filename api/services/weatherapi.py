import datetime
import os
import statistics

import requests


WEATHER_API_KEY = os.environ['WEATHER_API_KEY']
BASE_WEATHER_API_URL = os.environ['BASE_WEATHER_API_URL']

def extract_hourly_temps(day):
    """
    Extract hourly temps for the day and return as list.
    """
    temps = []
    for hour in day['hour']:
        temps.append(hour['temp_c'])
    return temps

def fetch_city_weather(city, days):
    """
    Fetch city weather data from weatherapi.com
    """
    end_date = datetime.datetime.now().date()
    start_date = end_date - datetime.timedelta(days=days)

    params = {
        'dt': start_date,
        'end_dt': end_date,
        'q': city,
        'key': WEATHER_API_KEY
    }
    return requests.get(BASE_WEATHER_API_URL, params=params)

def calculate_temps(city, days=0):
    """
    Calculates maximum, minimum, average and medium temps from hourly data
    collected over a range of `days`.
    """
    response = fetch_city_weather(city, days)
    if response.status_code != 200:
        return response.json(), response.status_code
    json_resp = response.json()
    forecast_day = json_resp['forecast']['forecastday']
    all_hourly_temps = []
    for day in forecast_day:
        temps = extract_hourly_temps(day)
        all_hourly_temps.extend(temps)
    maximum = max(all_hourly_temps)
    minimum = min(all_hourly_temps)
    average = statistics.mean(all_hourly_temps)
    median = statistics.median(all_hourly_temps)
    return {
        'maximum': maximum,
        'minimum': minimum,
        'average': average,
        'median': median
    }, response.status_code
