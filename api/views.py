import json
import logging

from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from api import serializers
from api.services import weatherapi


logger = logging.getLogger(__name__)


# Create your views here.
class WeatherDataList(APIView):
    """
    Get the maximum, minimum, average and median temperatures for a city
    over a period of days.
    """
    def post(self, request, city):
        data = {
            'city': city,
            'days': request.query_params.get('days')
        }
        input_serializer = serializers.InputSerializer(data=data)
        if input_serializer.is_valid():
            city = input_serializer.validated_data['city']
            days = input_serializer.validated_data['days']
            resp, status_code = weatherapi.calculate_temps(city, days)
            if status_code == 200:
                # wds: weather data serializer
                wds = serializers.WeatherDataSerializer(resp)
                return Response(wds.data, status=status.HTTP_200_OK)
            logger.error(json.dumps(resp))
            error = {'message': '500 Internal Server Error'}
            return Response(error, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return Response(input_serializer.errors, status.HTTP_400_BAD_REQUEST)
