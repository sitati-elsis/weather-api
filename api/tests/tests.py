import json
import os
import statistics

from unittest.mock import patch
from django.urls.exceptions import NoReverseMatch
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from api import serializers
from api.tests.weatherapi_mocks import success, error


class WeatherDataAPITestCase(APITestCase):
    def get_expected_temps(self, hourly_temps):
        """
        Calculates maximum, minimum, average and median temps from hourly_temps
        list.
        """
        total = sum(hourly_temps)
        count = len(hourly_temps)
        data = {
            'maximum': max(hourly_temps),
            'minimum': min(hourly_temps),
            'average': total/count,
            'median': statistics.median(hourly_temps)
        }
        wds = serializers.WeatherDataSerializer(data)
        return wds.data

    def extract_hourly_temps(self, json_response):
        """
        Extracts hourly temps (degree Celsius) from the json_response and
        returns them as a list.
        """
        hourly_temps = []
        for day in json_response['forecast']['forecastday']:
            for hour in day['hour']:
                temp = hour['temp_c']
                hourly_temps.append(temp)
        return hourly_temps

    @patch('requests.get', return_value=success.SevenDaysAPIResponseSuccess())
    def test_get_city_data_seven_days(self, mock_requests_get):
        """
        Ensure endpoint can get city data correctly.
        """
        url = reverse(
            'location-weather-data',
            kwargs={'city': 'athens'}
        ) + '?days=7'
        response = self.client.post(url)
        all_hourly_temps = self.extract_hourly_temps(
            success.SevenDaysAPIResponseSuccess().json())
        expected = self.get_expected_temps(all_hourly_temps)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), expected)

    @patch('requests.get', return_value=success.ThreeDayAPIResponseSuccess())
    def test_get_city_data_three_days(self, mock_requests_get):
        """
        Ensure endpoint can get city data correctly.
        """
        url = reverse(
            'location-weather-data',
            kwargs={'city': 'london'}
        ) + '?days=3'
        response = self.client.post(url)
        all_hourly_temps = self.extract_hourly_temps(
            success.ThreeDayAPIResponseSuccess().json())
        expected = self.get_expected_temps(all_hourly_temps)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), expected)

    @patch('requests.get', return_value=success.ZeroDayAPIResponseSuccess())
    def test_get_city_data_zero_days(self, mock_requests_get):
        """
        Ensure endpoint can get city data correctly.
        """
        url = reverse(
            'location-weather-data',
            kwargs={'city': 'accra'}
        ) + '?days=0'
        response = self.client.post(url)
        all_hourly_temps = self.extract_hourly_temps(
            success.ZeroDayAPIResponseSuccess().json())
        expected = self.get_expected_temps(all_hourly_temps)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), expected)

    @patch('requests.get', return_value=error.LocationDoesNotExistAPIResponse())
    def test_get_city_data_city_not_exist(self, mock_requests_get):
        """
        Test POST request on url when city does not exist.
        """
        url = reverse(
            'location-weather-data',
            kwargs={'city': 'sokovia'}
        ) + '?days=7'
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_500_INTERNAL_SERVER_ERROR)

    def test_malformed_request_no_city_param(self):
        """
        Test POST request on url with no city param.
        """
        with self.assertRaises(NoReverseMatch):
            url = reverse(
                'location-weather-data',
            ) + '?days=7'

    def test_malformed_request_no_day_param(self):
        """
        Test POST request on url with no day param.
        """
        url_missing_days = reverse(
            'location-weather-data',
            kwargs={'city': 'athens'}
        )
        response = self.client.post(url_missing_days)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.json()['days'][0], 'This field may not be null.')

    def test_malformed_request_invalid_day_param(self):
        """
        Test POST request on url when day param has value < 0.
        """
        url = reverse(
            'location-weather-data',
            kwargs={'city': 'sokovia'}
        ) + '?days=-1'
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json()['days'][0],
            'Ensure this value is greater than or equal to 0.'
        )

    def test_malformed_request_invalid_day_param_is_string(self):
        """
        Test POST request on url when day param has a string value.
        """
        url = reverse(
            'location-weather-data',
            kwargs={'city': 'sokovia'}
        ) + '?days=yesterday'
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(
            response.json()['days'][0],
            'A valid integer is required.'
        )
