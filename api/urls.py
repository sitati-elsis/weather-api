from django.urls import path
from django.views.generic import TemplateView
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.schemas import get_schema_view

from api.views import WeatherDataList
from api.schema_generators.query_params_schema_generator import DayQueryParamsSchemaGenerator


urlpatterns = [
    path('locations/<str:city>/', WeatherDataList.as_view(), name='location-weather-data'),
    path('openapi/', get_schema_view(
        title="Weather App.",
        description="API for city weather data",
        version="1.0.0",
        generator_class=DayQueryParamsSchemaGenerator
    ), name='openapi-schema'),
    path('docs/', TemplateView.as_view(
        template_name='swagger-ui.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='docs'),
]
