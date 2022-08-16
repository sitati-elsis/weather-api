class LocationDoesNotExistAPIResponse:
    """
    Mocks error response of weather data when location does not exist.
    """
    status_code = 400
    def json(self):
        return {
            "error": {
                "code": 1006,
                "message": "No matching location found."
            }
        }