from rest_framework import serializers


class InputSerializer(serializers.Serializer):
    """
    Serailizes input from local app.
    """
    city = serializers.CharField(write_only=True, required=True)
    days = serializers.IntegerField(write_only=True, default=0, min_value=0)

class WeatherDataSerializer(serializers.Serializer):
    """
    Serailizes weather data from external API.
    """
    maximum = serializers.DecimalField(
        read_only=True, max_digits=5, decimal_places=2)
    minimum = serializers.DecimalField(
        read_only=True, max_digits=5, decimal_places=2)
    average = serializers.DecimalField(
        read_only=True, max_digits=5, decimal_places=2)
    median = serializers.DecimalField(
        read_only=True, max_digits=5, decimal_places=2)
