from rest_framework.schemas.openapi import SchemaGenerator

class DayQueryParamsSchemaGenerator(SchemaGenerator):
    """
    Adds the `days` query parameter to the schema.
    """
    def get_schema(self, *args, **kwargs):
        schema = super().get_schema(*args, **kwargs)
        days = {
            'name': 'days',
            'in': 'query',
            'required': True,
            'description': 'Get city weather data over spanning over this number of days.',
            'schema': {
                'type': 'string'
            }
        }
        schema['paths']['/api/locations/{city}/']['post']['parameters'].append(days)
        return schema