class ZeroDayAPIResponseSuccess:
    """
    Mocks successful response of weather data from Accra (current day).
    """
    status_code = 200
    def json(self):
        return {
            "location": {
                "name": "Accra",
                "region": "Greater Accra",
                "country": "Ghana",
                "lat": 5.55,
                "lon": -0.22,
                "tz_id": "Africa/Accra",
                "localtime_epoch": 1660312594,
                "localtime": "2022-08-12 13:56"
            },
            "forecast": {
                "forecastday": [
                    {
                        "date": "2022-08-12",
                        "date_epoch": 1660262400,
                        "day": {
                            "maxtemp_c": 27.7,
                            "maxtemp_f": 81.9,
                            "mintemp_c": 22.1,
                            "mintemp_f": 71.8,
                            "avgtemp_c": 25.3,
                            "avgtemp_f": 77.5,
                        },
                        "hour": [
                            {
                                "time_epoch": 1660262400,
                                "time": "2022-08-12 00:00",
                                "temp_c": 23.5,
                                "temp_f": 74.3,
                            },
                            {
                                "time_epoch": 1660266000,
                                "time": "2022-08-12 01:00",
                                "temp_c": 23.3,
                                "temp_f": 73.9,
                            },
                            {
                                "time_epoch": 1660269600,
                                "time": "2022-08-12 02:00",
                                "temp_c": 23.1,
                                "temp_f": 73.6,
                            },
                            {
                                "time_epoch": 1660273200,
                                "time": "2022-08-12 03:00",
                                "temp_c": 22.9,
                                "temp_f": 73.2,
                            },
                            {
                                "time_epoch": 1660276800,
                                "time": "2022-08-12 04:00",
                                "temp_c": 22.6,
                                "temp_f": 72.7,
                            },
                            {
                                "time_epoch": 1660280400,
                                "time": "2022-08-12 05:00",
                                "temp_c": 22.4,
                                "temp_f": 72.3,
                            },
                            {
                                "time_epoch": 1660284000,
                                "time": "2022-08-12 06:00",
                                "temp_c": 22.1,
                                "temp_f": 71.8,
                            },
                            {
                                "time_epoch": 1660287600,
                                "time": "2022-08-12 07:00",
                                "temp_c": 23.0,
                                "temp_f": 73.5,
                            },
                            {
                                "time_epoch": 1660291200,
                                "time": "2022-08-12 08:00",
                                "temp_c": 24.0,
                                "temp_f": 75.1,
                            },
                            {
                                "time_epoch": 1660294800,
                                "time": "2022-08-12 09:00",
                                "temp_c": 24.9,
                                "temp_f": 76.8,
                            },
                            {
                                "time_epoch": 1660298400,
                                "time": "2022-08-12 10:00",
                                "temp_c": 25.8,
                                "temp_f": 78.5,
                            },
                            {
                                "time_epoch": 1660302000,
                                "time": "2022-08-12 11:00",
                                "temp_c": 26.8,
                                "temp_f": 80.2,
                            },
                            {
                                "time_epoch": 1660305600,
                                "time": "2022-08-12 12:00",
                                "temp_c": 27.7,
                                "temp_f": 81.9,
                            },
                            {
                                "time_epoch": 1660309200,
                                "time": "2022-08-12 13:00",
                                "temp_c": 27.3,
                                "temp_f": 81.1,
                            },
                            {
                                "time_epoch": 1660312800,
                                "time": "2022-08-12 14:00",
                                "temp_c": 26.9,
                                "temp_f": 80.4,
                            },
                            {
                                "time_epoch": 1660316400,
                                "time": "2022-08-12 15:00",
                                "temp_c": 26.5,
                                "temp_f": 79.7,
                            },
                            {
                                "time_epoch": 1660320000,
                                "time": "2022-08-12 16:00",
                                "temp_c": 26.1,
                                "temp_f": 79.0,
                            },
                            {
                                "time_epoch": 1660323600,
                                "time": "2022-08-12 17:00",
                                "temp_c": 25.7,
                                "temp_f": 78.3,
                            },
                            {
                                "time_epoch": 1660327200,
                                "time": "2022-08-12 18:00",
                                "temp_c": 25.3,
                                "temp_f": 77.5,
                            },
                            {
                                "time_epoch": 1660330800,
                                "time": "2022-08-12 19:00",
                                "temp_c": 25.0,
                                "temp_f": 77.1,
                            },
                            {
                                "time_epoch": 1660334400,
                                "time": "2022-08-12 20:00",
                                "temp_c": 24.8,
                                "temp_f": 76.6,
                            },
                            {
                                "time_epoch": 1660338000,
                                "time": "2022-08-12 21:00",
                                "temp_c": 24.5,
                                "temp_f": 76.1,
                            },
                            {
                                "time_epoch": 1660341600,
                                "time": "2022-08-12 22:00",
                                "temp_c": 24.1,
                                "temp_f": 75.4,
                            },
                            {
                                "time_epoch": 1660345200,
                                "time": "2022-08-12 23:00",
                                "temp_c": 23.7,
                                "temp_f": 74.7,
                            }
                        ]
                    }
                ]
            }
        }


class ThreeDayAPIResponseSuccess:
    """
    Mocks successful response of weather data from London (last 3 days).
    """
    status_code = 200
    def json(self):
        return {
            "location": {
                "name": "London",
                "region": "City of London, Greater London",
                "country": "United Kingdom",
                "lat": 51.52,
                "lon": -0.11,
                "tz_id": "Europe/London",
                "localtime_epoch": 1660310699,
                "localtime": "2022-08-12 14:24"
            },
            "forecast": {
                "forecastday": [
                    {
                        "date": "2022-08-10",
                        "date_epoch": 1660089600,
                        "day": {
                            "maxtemp_c": 30.5,
                            "maxtemp_f": 86.9,
                            "mintemp_c": 17.9,
                            "mintemp_f": 64.2,
                            "avgtemp_c": 25.8,
                            "avgtemp_f": 78.4,
                        },
                        "hour": [
                            {
                                "time_epoch": 1660086000,
                                "time": "2022-08-10 00:00",
                                "temp_c": 18.9,
                                "temp_f": 66.0,
                            },
                            {
                                "time_epoch": 1660089600,
                                "time": "2022-08-10 01:00",
                                "temp_c": 18.6,
                                "temp_f": 65.4,
                            },
                            {
                                "time_epoch": 1660093200,
                                "time": "2022-08-10 02:00",
                                "temp_c": 18.2,
                                "temp_f": 64.8,
                            },
                            {
                                "time_epoch": 1660096800,
                                "time": "2022-08-10 03:00",
                                "temp_c": 17.9,
                                "temp_f": 64.2,
                            },
                            {
                                "time_epoch": 1660100400,
                                "time": "2022-08-10 04:00",
                                "temp_c": 18.0,
                                "temp_f": 64.3,
                            },
                            {
                                "time_epoch": 1660104000,
                                "time": "2022-08-10 05:00",
                                "temp_c": 18.0,
                                "temp_f": 64.5,
                            },
                            {
                                "time_epoch": 1660107600,
                                "time": "2022-08-10 06:00",
                                "temp_c": 18.1,
                                "temp_f": 64.6,
                            },
                            {
                                "time_epoch": 1660111200,
                                "time": "2022-08-10 07:00",
                                "temp_c": 19.9,
                                "temp_f": 67.9,
                            },
                            {
                                "time_epoch": 1660114800,
                                "time": "2022-08-10 08:00",
                                "temp_c": 21.8,
                                "temp_f": 71.2,
                            },
                            {
                                "time_epoch": 1660118400,
                                "time": "2022-08-10 09:00",
                                "temp_c": 23.6,
                                "temp_f": 74.5,
                            },
                            {
                                "time_epoch": 1660122000,
                                "time": "2022-08-10 10:00",
                                "temp_c": 25.9,
                                "temp_f": 78.6,
                            },
                            {
                                "time_epoch": 1660125600,
                                "time": "2022-08-10 11:00",
                                "temp_c": 28.2,
                                "temp_f": 82.8,
                            },
                            {
                                "time_epoch": 1660129200,
                                "time": "2022-08-10 12:00",
                                "temp_c": 30.5,
                                "temp_f": 86.9,
                            },
                            {
                                "time_epoch": 1660132800,
                                "time": "2022-08-10 13:00",
                                "temp_c": 29.9,
                                "temp_f": 85.8,
                            },
                            {
                                "time_epoch": 1660136400,
                                "time": "2022-08-10 14:00",
                                "temp_c": 29.3,
                                "temp_f": 84.7,
                            },
                            {
                                "time_epoch": 1660140000,
                                "time": "2022-08-10 15:00",
                                "temp_c": 28.7,
                                "temp_f": 83.7,
                            },
                            {
                                "time_epoch": 1660143600,
                                "time": "2022-08-10 16:00",
                                "temp_c": 28.5,
                                "temp_f": 83.2,
                            },
                            {
                                "time_epoch": 1660147200,
                                "time": "2022-08-10 17:00",
                                "temp_c": 28.2,
                                "temp_f": 82.8,
                            },
                            {
                                "time_epoch": 1660150800,
                                "time": "2022-08-10 18:00",
                                "temp_c": 28.0,
                                "temp_f": 82.4,
                            },
                            {
                                "time_epoch": 1660154400,
                                "time": "2022-08-10 19:00",
                                "temp_c": 26.0,
                                "temp_f": 78.8,
                            },
                            {
                                "time_epoch": 1660158000,
                                "time": "2022-08-10 20:00",
                                "temp_c": 24.0,
                                "temp_f": 75.2,
                            },
                            {
                                "time_epoch": 1660161600,
                                "time": "2022-08-10 21:00",
                                "temp_c": 22.0,
                                "temp_f": 71.6,
                            },
                            {
                                "time_epoch": 1660165200,
                                "time": "2022-08-10 22:00",
                                "temp_c": 21.5,
                                "temp_f": 70.6,
                            },
                            {
                                "time_epoch": 1660168800,
                                "time": "2022-08-10 23:00",
                                "temp_c": 20.9,
                                "temp_f": 69.7,
                            }
                        ]
                    },
                    {
                        "date": "2022-08-11",
                        "date_epoch": 1660176000,
                        "day": {
                            "maxtemp_c": 34.3,
                            "maxtemp_f": 93.7,
                            "mintemp_c": 19.3,
                            "mintemp_f": 66.7,
                            "avgtemp_c": 28.3,
                            "avgtemp_f": 82.9,
                        },
                        "hour": [
                            {
                                "time_epoch": 1660172400,
                                "time": "2022-08-11 00:00",
                                "temp_c": 20.4,
                                "temp_f": 68.7,
                            },
                            {
                                "time_epoch": 1660176000,
                                "time": "2022-08-11 01:00",
                                "temp_c": 20.0,
                                "temp_f": 68.1,
                            },
                            {
                                "time_epoch": 1660179600,
                                "time": "2022-08-11 02:00",
                                "temp_c": 19.7,
                                "temp_f": 67.4,
                            },
                            {
                                "time_epoch": 1660183200,
                                "time": "2022-08-11 03:00",
                                "temp_c": 19.3,
                                "temp_f": 66.7,
                            },
                            {
                                "time_epoch": 1660186800,
                                "time": "2022-08-11 04:00",
                                "temp_c": 19.4,
                                "temp_f": 66.9,
                            },
                            {
                                "time_epoch": 1660190400,
                                "time": "2022-08-11 05:00",
                                "temp_c": 19.5,
                                "temp_f": 67.1,
                            },
                            {
                                "time_epoch": 1660194000,
                                "time": "2022-08-11 06:00",
                                "temp_c": 19.6,
                                "temp_f": 67.3,
                            },
                            {
                                "time_epoch": 1660197600,
                                "time": "2022-08-11 07:00",
                                "temp_c": 21.8,
                                "temp_f": 71.2,
                            },
                            {
                                "time_epoch": 1660201200,
                                "time": "2022-08-11 08:00",
                                "temp_c": 23.9,
                                "temp_f": 75.1,
                            },
                            {
                                "time_epoch": 1660204800,
                                "time": "2022-08-11 09:00",
                                "temp_c": 26.1,
                                "temp_f": 79.0,
                            },
                            {
                                "time_epoch": 1660208400,
                                "time": "2022-08-11 10:00",
                                "temp_c": 28.8,
                                "temp_f": 83.9,
                            },
                            {
                                "time_epoch": 1660212000,
                                "time": "2022-08-11 11:00",
                                "temp_c": 31.6,
                                "temp_f": 88.8,
                            },
                            {
                                "time_epoch": 1660215600,
                                "time": "2022-08-11 12:00",
                                "temp_c": 34.3,
                                "temp_f": 93.7,
                            },
                            {
                                "time_epoch": 1660219200,
                                "time": "2022-08-11 13:00",
                                "temp_c": 33.5,
                                "temp_f": 92.4,
                            },
                            {
                                "time_epoch": 1660222800,
                                "time": "2022-08-11 14:00",
                                "temp_c": 32.8,
                                "temp_f": 91.0,
                            },
                            {
                                "time_epoch": 1660226400,
                                "time": "2022-08-11 15:00",
                                "temp_c": 32.0,
                                "temp_f": 89.6,
                            },
                            {
                                "time_epoch": 1660230000,
                                "time": "2022-08-11 16:00",
                                "temp_c": 31.1,
                                "temp_f": 88.0,
                            },
                            {
                                "time_epoch": 1660233600,
                                "time": "2022-08-11 17:00",
                                "temp_c": 30.3,
                                "temp_f": 86.5,
                            },
                            {
                                "time_epoch": 1660237200,
                                "time": "2022-08-11 18:00",
                                "temp_c": 29.4,
                                "temp_f": 84.9,
                            },
                            {
                                "time_epoch": 1660240800,
                                "time": "2022-08-11 19:00",
                                "temp_c": 27.7,
                                "temp_f": 81.9,
                            },
                            {
                                "time_epoch": 1660244400,
                                "time": "2022-08-11 20:00",
                                "temp_c": 26.1,
                                "temp_f": 78.9,
                            },
                            {
                                "time_epoch": 1660248000,
                                "time": "2022-08-11 21:00",
                                "temp_c": 24.4,
                                "temp_f": 75.9,
                            },
                            {
                                "time_epoch": 1660251600,
                                "time": "2022-08-11 22:00",
                                "temp_c": 23.6,
                                "temp_f": 74.5,
                            },
                            {
                                "time_epoch": 1660255200,
                                "time": "2022-08-11 23:00",
                                "temp_c": 22.8,
                                "temp_f": 73.0,
                            }
                        ]
                    },
                    {
                        "date": "2022-08-12",
                        "date_epoch": 1660262400,
                        "day": {
                            "maxtemp_c": 35.4,
                            "maxtemp_f": 95.7,
                            "mintemp_c": 20.6,
                            "mintemp_f": 69.1,
                            "avgtemp_c": 29.3,
                            "avgtemp_f": 84.7,
                        },
                        "hour": [
                            {
                                "time_epoch": 1660258800,
                                "time": "2022-08-12 00:00",
                                "temp_c": 22.0,
                                "temp_f": 71.6,
                            },
                            {
                                "time_epoch": 1660262400,
                                "time": "2022-08-12 01:00",
                                "temp_c": 21.5,
                                "temp_f": 70.8,
                            },
                            {
                                "time_epoch": 1660266000,
                                "time": "2022-08-12 02:00",
                                "temp_c": 21.1,
                                "temp_f": 69.9,
                            },
                            {
                                "time_epoch": 1660269600,
                                "time": "2022-08-12 03:00",
                                "temp_c": 20.6,
                                "temp_f": 69.1,
                            },
                            {
                                "time_epoch": 1660273200,
                                "time": "2022-08-12 04:00",
                                "temp_c": 20.6,
                                "temp_f": 69.1,
                            },
                            {
                                "time_epoch": 1660276800,
                                "time": "2022-08-12 05:00",
                                "temp_c": 20.6,
                                "temp_f": 69.1,
                            },
                            {
                                "time_epoch": 1660280400,
                                "time": "2022-08-12 06:00",
                                "temp_c": 20.6,
                                "temp_f": 69.1,
                            },
                            {
                                "time_epoch": 1660284000,
                                "time": "2022-08-12 07:00",
                                "temp_c": 22.7,
                                "temp_f": 72.9,
                            },
                            {
                                "time_epoch": 1660287600,
                                "time": "2022-08-12 08:00",
                                "temp_c": 24.8,
                                "temp_f": 76.6,
                            },
                            {
                                "time_epoch": 1660291200,
                                "time": "2022-08-12 09:00",
                                "temp_c": 26.9,
                                "temp_f": 80.4,
                            },
                            {
                                "time_epoch": 1660294800,
                                "time": "2022-08-12 10:00",
                                "temp_c": 29.7,
                                "temp_f": 85.5,
                            },
                            {
                                "time_epoch": 1660298400,
                                "time": "2022-08-12 11:00",
                                "temp_c": 32.6,
                                "temp_f": 90.6,
                            },
                            {
                                "time_epoch": 1660302000,
                                "time": "2022-08-12 12:00",
                                "temp_c": 35.4,
                                "temp_f": 95.7,
                            },
                            {
                                "time_epoch": 1660305600,
                                "time": "2022-08-12 13:00",
                                "temp_c": 34.7,
                                "temp_f": 94.5,
                            },
                            {
                                "time_epoch": 1660309200,
                                "time": "2022-08-12 14:00",
                                "temp_c": 34.0,
                                "temp_f": 93.2,
                            },
                            {
                                "time_epoch": 1660312800,
                                "time": "2022-08-12 15:00",
                                "temp_c": 33.3,
                                "temp_f": 91.9,
                            },
                            {
                                "time_epoch": 1660316400,
                                "time": "2022-08-12 16:00",
                                "temp_c": 32.3,
                                "temp_f": 90.1,
                            },
                            {
                                "time_epoch": 1660320000,
                                "time": "2022-08-12 17:00",
                                "temp_c": 31.3,
                                "temp_f": 88.3,
                            },
                            {
                                "time_epoch": 1660323600,
                                "time": "2022-08-12 18:00",
                                "temp_c": 30.3,
                                "temp_f": 86.5,
                            },
                            {
                                "time_epoch": 1660327200,
                                "time": "2022-08-12 19:00",
                                "temp_c": 28.6,
                                "temp_f": 83.5,
                            },
                            {
                                "time_epoch": 1660330800,
                                "time": "2022-08-12 20:00",
                                "temp_c": 26.9,
                                "temp_f": 80.4,
                            },
                            {
                                "time_epoch": 1660334400,
                                "time": "2022-08-12 21:00",
                                "temp_c": 25.2,
                                "temp_f": 77.4,
                            },
                            {
                                "time_epoch": 1660338000,
                                "time": "2022-08-12 22:00",
                                "temp_c": 24.3,
                                "temp_f": 75.8,
                            },
                            {
                                "time_epoch": 1660341600,
                                "time": "2022-08-12 23:00",
                                "temp_c": 23.5,
                                "temp_f": 74.2,
                            }
                        ]
                    }
                ]
            }
        }


class SevenDaysAPIResponseSuccess:
    """
    Mocks successful response of weather data from Greece (last 7 days).
    """
    status_code = 200
    def json(self):
        return {
            "location": {
                "name": "Athens",
                "region": "Attica",
                "country": "Greece",
                "lat": 37.98,
                "lon": 23.72,
                "tz_id": "Europe/Athens",
                "localtime_epoch": 1660244270,
                "localtime": "2022-08-11 21:57"
            },
            "forecast": {
                "forecastday": [
                    {
                        "date": "2022-08-05",
                        "date_epoch": 1659657600,
                        "day": {
                            "maxtemp_c": 36.6,
                            "maxtemp_f": 97.9,
                            "mintemp_c": 25.0,
                            "mintemp_f": 77.0,
                            "avgtemp_c": 32.3,
                            "avgtemp_f": 90.1,
                        },
                        "hour": [
                            {
                                "time_epoch": 1659646800,
                                "time": "2022-08-05 00:00",
                                "temp_c": 25.8,
                                "temp_f": 78.4
                            },
                            {
                                "time_epoch": 1659650400,
                                "time": "2022-08-05 01:00",
                                "temp_c": 25.7,
                                "temp_f": 78.3,
                            },
                            {
                                "time_epoch": 1659654000,
                                "time": "2022-08-05 02:00",
                                "temp_c": 25.6,
                                "temp_f": 78.1,
                            },
                            {
                                "time_epoch": 1659657600,
                                "time": "2022-08-05 03:00",
                                "temp_c": 25.5,
                                "temp_f": 77.9,
                            },
                            {
                                "time_epoch": 1659661200,
                                "time": "2022-08-05 04:00",
                                "temp_c": 25.3,
                                "temp_f": 77.6,
                            },
                            {
                                "time_epoch": 1659664800,
                                "time": "2022-08-05 05:00",
                                "temp_c": 25.2,
                                "temp_f": 77.3,
                            },
                            {
                                "time_epoch": 1659668400,
                                "time": "2022-08-05 06:00",
                                "temp_c": 25.0,
                                "temp_f": 77.0,
                            },
                            {
                                "time_epoch": 1659672000,
                                "time": "2022-08-05 07:00",
                                "temp_c": 26.8,
                                "temp_f": 80.2,
                            },
                            {
                                "time_epoch": 1659675600,
                                "time": "2022-08-05 08:00",
                                "temp_c": 28.5,
                                "temp_f": 83.4,
                            },
                            {
                                "time_epoch": 1659679200,
                                "time": "2022-08-05 09:00",
                                "temp_c": 30.3,
                                "temp_f": 86.5,
                            },
                            {
                                "time_epoch": 1659682800,
                                "time": "2022-08-05 10:00",
                                "temp_c": 32.2,
                                "temp_f": 90.0,
                            },
                            {
                                "time_epoch": 1659686400,
                                "time": "2022-08-05 11:00",
                                "temp_c": 34.1,
                                "temp_f": 93.4,
                            },
                            {
                                "time_epoch": 1659690000,
                                "time": "2022-08-05 12:00",
                                "temp_c": 36.0,
                                "temp_f": 96.8,
                            },
                            {
                                "time_epoch": 1659693600,
                                "time": "2022-08-05 13:00",
                                "temp_c": 36.2,
                                "temp_f": 97.2,
                            },
                            {
                                "time_epoch": 1659697200,
                                "time": "2022-08-05 14:00",
                                "temp_c": 36.4,
                                "temp_f": 97.5,
                            },
                            {
                                "time_epoch": 1659700800,
                                "time": "2022-08-05 15:00",
                                "temp_c": 36.6,
                                "temp_f": 97.9,
                            },
                            {
                                "time_epoch": 1659704400,
                                "time": "2022-08-05 16:00",
                                "temp_c": 35.6,
                                "temp_f": 96.1,
                            },
                            {
                                "time_epoch": 1659708000,
                                "time": "2022-08-05 17:00",
                                "temp_c": 34.6,
                                "temp_f": 94.3,
                            },
                            {
                                "time_epoch": 1659711600,
                                "time": "2022-08-05 18:00",
                                "temp_c": 33.6,
                                "temp_f": 92.5,
                            },
                            {
                                "time_epoch": 1659715200,
                                "time": "2022-08-05 19:00",
                                "temp_c": 31.7,
                                "temp_f": 89.0,
                            },
                            {
                                "time_epoch": 1659718800,
                                "time": "2022-08-05 20:00",
                                "temp_c": 29.7,
                                "temp_f": 85.5,
                            },
                            {
                                "time_epoch": 1659722400,
                                "time": "2022-08-05 21:00",
                                "temp_c": 27.8,
                                "temp_f": 82.0,
                            },
                            {
                                "time_epoch": 1659726000,
                                "time": "2022-08-05 22:00",
                                "temp_c": 26.9,
                                "temp_f": 80.5,
                            },
                            {
                                "time_epoch": 1659729600,
                                "time": "2022-08-05 23:00",
                                "temp_c": 26.1,
                                "temp_f": 78.9,
                            }
                        ]
                    },
                    {
                        "date": "2022-08-06",
                        "date_epoch": 1659744000,
                        "day": {
                            "maxtemp_c": 36.4,
                            "maxtemp_f": 97.5,
                            "mintemp_c": 23.4,
                            "mintemp_f": 74.1,
                            "avgtemp_c": 32.0,
                            "avgtemp_f": 89.7,
                        },
                        "hour": [
                            {
                                "time_epoch": 1659733200,
                                "time": "2022-08-06 00:00",
                                "temp_c": 25.2,
                                "temp_f": 77.4,
                            },
                            {
                                "time_epoch": 1659736800,
                                "time": "2022-08-06 01:00",
                                "temp_c": 24.9,
                                "temp_f": 76.8,
                            },
                            {
                                "time_epoch": 1659740400,
                                "time": "2022-08-06 02:00",
                                "temp_c": 24.5,
                                "temp_f": 76.2,
                            },
                            {
                                "time_epoch": 1659744000,
                                "time": "2022-08-06 03:00",
                                "temp_c": 24.2,
                                "temp_f": 75.6,
                            },
                            {
                                "time_epoch": 1659747600,
                                "time": "2022-08-06 04:00",
                                "temp_c": 23.9,
                                "temp_f": 75.1,
                            },
                            {
                                "time_epoch": 1659751200,
                                "time": "2022-08-06 05:00",
                                "temp_c": 23.7,
                                "temp_f": 74.6,
                            },
                            {
                                "time_epoch": 1659754800,
                                "time": "2022-08-06 06:00",
                                "temp_c": 23.4,
                                "temp_f": 74.1,
                            },
                            {
                                "time_epoch": 1659758400,
                                "time": "2022-08-06 07:00",
                                "temp_c": 25.8,
                                "temp_f": 78.4,
                            },
                            {
                                "time_epoch": 1659762000,
                                "time": "2022-08-06 08:00",
                                "temp_c": 28.1,
                                "temp_f": 82.6,
                            },
                            {
                                "time_epoch": 1659765600,
                                "time": "2022-08-06 09:00",
                                "temp_c": 30.5,
                                "temp_f": 86.9,
                            },
                            {
                                "time_epoch": 1659769200,
                                "time": "2022-08-06 10:00",
                                "temp_c": 32.4,
                                "temp_f": 90.3,
                            },
                            {
                                "time_epoch": 1659772800,
                                "time": "2022-08-06 11:00",
                                "temp_c": 34.3,
                                "temp_f": 93.7,
                            },
                            {
                                "time_epoch": 1659776400,
                                "time": "2022-08-06 12:00",
                                "temp_c": 36.2,
                                "temp_f": 97.2,
                            },
                            {
                                "time_epoch": 1659780000,
                                "time": "2022-08-06 13:00",
                                "temp_c": 36.3,
                                "temp_f": 97.3,
                            },
                            {
                                "time_epoch": 1659783600,
                                "time": "2022-08-06 14:00",
                                "temp_c": 36.3,
                                "temp_f": 97.4,
                            },
                            {
                                "time_epoch": 1659787200,
                                "time": "2022-08-06 15:00",
                                "temp_c": 36.4,
                                "temp_f": 97.5,
                            },
                            {
                                "time_epoch": 1659790800,
                                "time": "2022-08-06 16:00",
                                "temp_c": 35.5,
                                "temp_f": 95.9,
                            },
                            {
                                "time_epoch": 1659794400,
                                "time": "2022-08-06 17:00",
                                "temp_c": 34.6,
                                "temp_f": 94.3,
                            },
                            {
                                "time_epoch": 1659798000,
                                "time": "2022-08-06 18:00",
                                "temp_c": 33.7,
                                "temp_f": 92.7,
                            },
                            {
                                "time_epoch": 1659801600,
                                "time": "2022-08-06 19:00",
                                "temp_c": 31.4,
                                "temp_f": 88.5,
                            },
                            {
                                "time_epoch": 1659805200,
                                "time": "2022-08-06 20:00",
                                "temp_c": 29.0,
                                "temp_f": 84.3,
                            },
                            {
                                "time_epoch": 1659808800,
                                "time": "2022-08-06 21:00",
                                "temp_c": 26.7,
                                "temp_f": 80.1,
                            },
                            {
                                "time_epoch": 1659812400,
                                "time": "2022-08-06 22:00",
                                "temp_c": 26.4,
                                "temp_f": 79.6,
                            },
                            {
                                "time_epoch": 1659816000,
                                "time": "2022-08-06 23:00",
                                "temp_c": 26.2,
                                "temp_f": 79.1,
                            }
                        ]
                    },
                    {
                        "date": "2022-08-07",
                        "date_epoch": 1659830400,
                        "day": {
                            "maxtemp_c": 34.7,
                            "maxtemp_f": 94.5,
                            "mintemp_c": 23.7,
                            "mintemp_f": 74.7,
                            "avgtemp_c": 30.9,
                            "avgtemp_f": 87.6,
                        },
                        "hour": [
                            {
                                "time_epoch": 1659819600,
                                "time": "2022-08-07 00:00",
                                "temp_c": 25.9,
                                "temp_f": 78.6,
                            },
                            {
                                "time_epoch": 1659823200,
                                "time": "2022-08-07 01:00",
                                "temp_c": 25.6,
                                "temp_f": 78.0,
                            },
                            {
                                "time_epoch": 1659826800,
                                "time": "2022-08-07 02:00",
                                "temp_c": 25.2,
                                "temp_f": 77.4,
                            },
                            {
                                "time_epoch": 1659830400,
                                "time": "2022-08-07 03:00",
                                "temp_c": 24.9,
                                "temp_f": 76.8,
                            },
                            {
                                "time_epoch": 1659834000,
                                "time": "2022-08-07 04:00",
                                "temp_c": 24.5,
                                "temp_f": 76.1,
                            },
                            {
                                "time_epoch": 1659837600,
                                "time": "2022-08-07 05:00",
                                "temp_c": 24.1,
                                "temp_f": 75.4,
                            },
                            {
                                "time_epoch": 1659841200,
                                "time": "2022-08-07 06:00",
                                "temp_c": 23.7,
                                "temp_f": 74.7,
                            },
                            {
                                "time_epoch": 1659844800,
                                "time": "2022-08-07 07:00",
                                "temp_c": 25.5,
                                "temp_f": 78.0,
                            },
                            {
                                "time_epoch": 1659848400,
                                "time": "2022-08-07 08:00",
                                "temp_c": 27.4,
                                "temp_f": 81.3,
                            },
                            {
                                "time_epoch": 1659852000,
                                "time": "2022-08-07 09:00",
                                "temp_c": 29.2,
                                "temp_f": 84.6,
                            },
                            {
                                "time_epoch": 1659855600,
                                "time": "2022-08-07 10:00",
                                "temp_c": 30.9,
                                "temp_f": 87.7,
                            },
                            {
                                "time_epoch": 1659859200,
                                "time": "2022-08-07 11:00",
                                "temp_c": 32.7,
                                "temp_f": 90.8,
                            },
                            {
                                "time_epoch": 1659862800,
                                "time": "2022-08-07 12:00",
                                "temp_c": 34.4,
                                "temp_f": 93.9,
                            },
                            {
                                "time_epoch": 1659866400,
                                "time": "2022-08-07 13:00",
                                "temp_c": 34.5,
                                "temp_f": 94.1,
                            },
                            {
                                "time_epoch": 1659870000,
                                "time": "2022-08-07 14:00",
                                "temp_c": 34.6,
                                "temp_f": 94.3,
                            },
                            {
                                "time_epoch": 1659873600,
                                "time": "2022-08-07 15:00",
                                "temp_c": 34.7,
                                "temp_f": 94.5,
                            },
                            {
                                "time_epoch": 1659877200,
                                "time": "2022-08-07 16:00",
                                "temp_c": 34.0,
                                "temp_f": 93.1,
                            },
                            {
                                "time_epoch": 1659880800,
                                "time": "2022-08-07 17:00",
                                "temp_c": 33.2,
                                "temp_f": 91.8,
                            },
                            {
                                "time_epoch": 1659884400,
                                "time": "2022-08-07 18:00",
                                "temp_c": 32.5,
                                "temp_f": 90.5,
                            },
                            {
                                "time_epoch": 1659888000,
                                "time": "2022-08-07 19:00",
                                "temp_c": 30.4,
                                "temp_f": 86.7,
                            },
                            {
                                "time_epoch": 1659891600,
                                "time": "2022-08-07 20:00",
                                "temp_c": 28.2,
                                "temp_f": 82.8,
                            },
                            {
                                "time_epoch": 1659895200,
                                "time": "2022-08-07 21:00",
                                "temp_c": 26.1,
                                "temp_f": 79.0,
                            },
                            {
                                "time_epoch": 1659898800,
                                "time": "2022-08-07 22:00",
                                "temp_c": 25.9,
                                "temp_f": 78.6,
                            },
                            {
                                "time_epoch": 1659902400,
                                "time": "2022-08-07 23:00",
                                "temp_c": 25.7,
                                "temp_f": 78.3,
                            }
                        ]
                    },
                    {
                        "date": "2022-08-08",
                        "date_epoch": 1659916800,
                        "day": {
                            "maxtemp_c": 35.8,
                            "maxtemp_f": 96.4,
                            "mintemp_c": 23.6,
                            "mintemp_f": 74.5,
                            "avgtemp_c": 31.3,
                            "avgtemp_f": 88.4,
                        },
                        "hour": [
                            {
                                "time_epoch": 1659906000,
                                "time": "2022-08-08 00:00",
                                "temp_c": 25.5,
                                "temp_f": 77.9,
                            },
                            {
                                "time_epoch": 1659909600,
                                "time": "2022-08-08 01:00",
                                "temp_c": 24.9,
                                "temp_f": 76.9,
                            },
                            {
                                "time_epoch": 1659913200,
                                "time": "2022-08-08 02:00",
                                "temp_c": 24.4,
                                "temp_f": 75.9,
                            },
                            {
                                "time_epoch": 1659916800,
                                "time": "2022-08-08 03:00",
                                "temp_c": 23.8,
                                "temp_f": 74.8,
                            },
                            {
                                "time_epoch": 1659920400,
                                "time": "2022-08-08 04:00",
                                "temp_c": 23.7,
                                "temp_f": 74.7,
                            },
                            {
                                "time_epoch": 1659924000,
                                "time": "2022-08-08 05:00",
                                "temp_c": 23.7,
                                "temp_f": 74.6,
                            },
                            {
                                "time_epoch": 1659927600,
                                "time": "2022-08-08 06:00",
                                "temp_c": 23.6,
                                "temp_f": 74.5,
                            },
                            {
                                "time_epoch": 1659931200,
                                "time": "2022-08-08 07:00",
                                "temp_c": 25.5,
                                "temp_f": 77.8,
                            },
                            {
                                "time_epoch": 1659934800,
                                "time": "2022-08-08 08:00",
                                "temp_c": 27.3,
                                "temp_f": 81.2,
                            },
                            {
                                "time_epoch": 1659938400,
                                "time": "2022-08-08 09:00",
                                "temp_c": 29.2,
                                "temp_f": 84.6,
                            },
                            {
                                "time_epoch": 1659942000,
                                "time": "2022-08-08 10:00",
                                "temp_c": 30.9,
                                "temp_f": 87.6,
                            },
                            {
                                "time_epoch": 1659945600,
                                "time": "2022-08-08 11:00",
                                "temp_c": 32.6,
                                "temp_f": 90.7,
                            },
                            {
                                "time_epoch": 1659949200,
                                "time": "2022-08-08 12:00",
                                "temp_c": 34.3,
                                "temp_f": 93.7,
                            },
                            {
                                "time_epoch": 1659952800,
                                "time": "2022-08-08 13:00",
                                "temp_c": 34.8,
                                "temp_f": 94.6,
                            },
                            {
                                "time_epoch": 1659956400,
                                "time": "2022-08-08 14:00",
                                "temp_c": 35.3,
                                "temp_f": 95.5,
                            },
                            {
                                "time_epoch": 1659960000,
                                "time": "2022-08-08 15:00",
                                "temp_c": 35.8,
                                "temp_f": 96.4,
                            },
                            {
                                "time_epoch": 1659963600,
                                "time": "2022-08-08 16:00",
                                "temp_c": 35.1,
                                "temp_f": 95.2,
                            },
                            {
                                "time_epoch": 1659967200,
                                "time": "2022-08-08 17:00",
                                "temp_c": 34.5,
                                "temp_f": 94.0,
                            },
                            {
                                "time_epoch": 1659970800,
                                "time": "2022-08-08 18:00",
                                "temp_c": 33.8,
                                "temp_f": 92.8,
                            },
                            {
                                "time_epoch": 1659974400,
                                "time": "2022-08-08 19:00",
                                "temp_c": 31.5,
                                "temp_f": 88.6,
                            },
                            {
                                "time_epoch": 1659978000,
                                "time": "2022-08-08 20:00",
                                "temp_c": 29.1,
                                "temp_f": 84.4,
                            },
                            {
                                "time_epoch": 1659981600,
                                "time": "2022-08-08 21:00",
                                "temp_c": 26.8,
                                "temp_f": 80.2,
                            },
                            {
                                "time_epoch": 1659985200,
                                "time": "2022-08-08 22:00",
                                "temp_c": 26.4,
                                "temp_f": 79.6,
                            },
                            {
                                "time_epoch": 1659988800,
                                "time": "2022-08-08 23:00",
                                "temp_c": 26.1,
                                "temp_f": 78.9,
                            }
                        ]
                    },
                    {
                        "date": "2022-08-09",
                        "date_epoch": 1660003200,
                        "day": {
                            "maxtemp_c": 35.6,
                            "maxtemp_f": 96.1,
                            "mintemp_c": 24.1,
                            "mintemp_f": 75.4,
                            "avgtemp_c": 31.5,
                            "avgtemp_f": 88.8,
                        },
                        "hour": [
                            {
                                "time_epoch": 1659992400,
                                "time": "2022-08-09 00:00",
                                "temp_c": 25.7,
                                "temp_f": 78.3,
                            },
                            {
                                "time_epoch": 1659996000,
                                "time": "2022-08-09 01:00",
                                "temp_c": 25.3,
                                "temp_f": 77.5,
                            },
                            {
                                "time_epoch": 1659999600,
                                "time": "2022-08-09 02:00",
                                "temp_c": 24.9,
                                "temp_f": 76.8,
                            },
                            {
                                "time_epoch": 1660003200,
                                "time": "2022-08-09 03:00",
                                "temp_c": 24.5,
                                "temp_f": 76.1,
                            },
                            {
                                "time_epoch": 1660006800,
                                "time": "2022-08-09 04:00",
                                "temp_c": 24.4,
                                "temp_f": 75.9,
                            },
                            {
                                "time_epoch": 1660010400,
                                "time": "2022-08-09 05:00",
                                "temp_c": 24.2,
                                "temp_f": 75.6,
                            },
                            {
                                "time_epoch": 1660014000,
                                "time": "2022-08-09 06:00",
                                "temp_c": 24.1,
                                "temp_f": 75.4,
                            },
                            {
                                "time_epoch": 1660017600,
                                "time": "2022-08-09 07:00",
                                "temp_c": 25.9,
                                "temp_f": 78.7,
                            },
                            {
                                "time_epoch": 1660021200,
                                "time": "2022-08-09 08:00",
                                "temp_c": 27.8,
                                "temp_f": 82.0,
                            },
                            {
                                "time_epoch": 1660024800,
                                "time": "2022-08-09 09:00",
                                "temp_c": 29.6,
                                "temp_f": 85.3,
                            },
                            {
                                "time_epoch": 1660028400,
                                "time": "2022-08-09 10:00",
                                "temp_c": 31.4,
                                "temp_f": 88.5,
                            },
                            {
                                "time_epoch": 1660032000,
                                "time": "2022-08-09 11:00",
                                "temp_c": 33.1,
                                "temp_f": 91.6,
                            },
                            {
                                "time_epoch": 1660035600,
                                "time": "2022-08-09 12:00",
                                "temp_c": 34.9,
                                "temp_f": 94.8,
                            },
                            {
                                "time_epoch": 1660039200,
                                "time": "2022-08-09 13:00",
                                "temp_c": 35.1,
                                "temp_f": 95.2,
                            },
                            {
                                "time_epoch": 1660042800,
                                "time": "2022-08-09 14:00",
                                "temp_c": 35.4,
                                "temp_f": 95.7,
                            },
                            {
                                "time_epoch": 1660046400,
                                "time": "2022-08-09 15:00",
                                "temp_c": 35.6,
                                "temp_f": 96.1,
                            },
                            {
                                "time_epoch": 1660050000,
                                "time": "2022-08-09 16:00",
                                "temp_c": 34.9,
                                "temp_f": 94.8,
                            },
                            {
                                "time_epoch": 1660053600,
                                "time": "2022-08-09 17:00",
                                "temp_c": 34.2,
                                "temp_f": 93.6,
                            },
                            {
                                "time_epoch": 1660057200,
                                "time": "2022-08-09 18:00",
                                "temp_c": 33.5,
                                "temp_f": 92.3,
                            },
                            {
                                "time_epoch": 1660060800,
                                "time": "2022-08-09 19:00",
                                "temp_c": 31.2,
                                "temp_f": 88.2,
                            },
                            {
                                "time_epoch": 1660064400,
                                "time": "2022-08-09 20:00",
                                "temp_c": 28.9,
                                "temp_f": 84.0,
                            },
                            {
                                "time_epoch": 1660068000,
                                "time": "2022-08-09 21:00",
                                "temp_c": 26.6,
                                "temp_f": 79.9,
                            },
                            {
                                "time_epoch": 1660071600,
                                "time": "2022-08-09 22:00",
                                "temp_c": 26.1,
                                "temp_f": 79.0,
                            },
                            {
                                "time_epoch": 1660075200,
                                "time": "2022-08-09 23:00",
                                "temp_c": 25.7,
                                "temp_f": 78.2,
                            }
                        ]
                    },
                    {
                        "date": "2022-08-10",
                        "date_epoch": 1660089600,
                        "day": {
                            "maxtemp_c": 36.5,
                            "maxtemp_f": 97.7,
                            "mintemp_c": 22.5,
                            "mintemp_f": 72.5,
                            "avgtemp_c": 31.7,
                            "avgtemp_f": 89.1,
                        },
                        "hour": [
                            {
                                "time_epoch": 1660078800,
                                "time": "2022-08-10 00:00",
                                "temp_c": 25.2,
                                "temp_f": 77.4,
                            },
                            {
                                "time_epoch": 1660082400,
                                "time": "2022-08-10 01:00",
                                "temp_c": 24.8,
                                "temp_f": 76.6,
                            },
                            {
                                "time_epoch": 1660086000,
                                "time": "2022-08-10 02:00",
                                "temp_c": 24.4,
                                "temp_f": 75.9,
                            },
                            {
                                "time_epoch": 1660089600,
                                "time": "2022-08-10 03:00",
                                "temp_c": 24.0,
                                "temp_f": 75.2,
                            },
                            {
                                "time_epoch": 1660093200,
                                "time": "2022-08-10 04:00",
                                "temp_c": 23.5,
                                "temp_f": 74.3,
                            },
                            {
                                "time_epoch": 1660096800,
                                "time": "2022-08-10 05:00",
                                "temp_c": 23.0,
                                "temp_f": 73.4,
                            },
                            {
                                "time_epoch": 1660100400,
                                "time": "2022-08-10 06:00",
                                "temp_c": 22.5,
                                "temp_f": 72.5,
                            },
                            {
                                "time_epoch": 1660104000,
                                "time": "2022-08-10 07:00",
                                "temp_c": 25.1,
                                "temp_f": 77.2,
                            },
                            {
                                "time_epoch": 1660107600,
                                "time": "2022-08-10 08:00",
                                "temp_c": 27.8,
                                "temp_f": 82.0,
                            },
                            {
                                "time_epoch": 1660111200,
                                "time": "2022-08-10 09:00",
                                "temp_c": 30.4,
                                "temp_f": 86.7,
                            },
                            {
                                "time_epoch": 1660114800,
                                "time": "2022-08-10 10:00",
                                "temp_c": 32.4,
                                "temp_f": 90.3,
                            },
                            {
                                "time_epoch": 1660118400,
                                "time": "2022-08-10 11:00",
                                "temp_c": 34.3,
                                "temp_f": 93.8,
                            },
                            {
                                "time_epoch": 1660122000,
                                "time": "2022-08-10 12:00",
                                "temp_c": 36.3,
                                "temp_f": 97.3,
                            },
                            {
                                "time_epoch": 1660125600,
                                "time": "2022-08-10 13:00",
                                "temp_c": 36.4,
                                "temp_f": 97.5,
                            },
                            {
                                "time_epoch": 1660129200,
                                "time": "2022-08-10 14:00",
                                "temp_c": 36.4,
                                "temp_f": 97.6,
                            },
                            {
                                "time_epoch": 1660132800,
                                "time": "2022-08-10 15:00",
                                "temp_c": 36.5,
                                "temp_f": 97.7,
                            },
                            {
                                "time_epoch": 1660136400,
                                "time": "2022-08-10 16:00",
                                "temp_c": 35.3,
                                "temp_f": 95.6,
                            },
                            {
                                "time_epoch": 1660140000,
                                "time": "2022-08-10 17:00",
                                "temp_c": 34.2,
                                "temp_f": 93.5,
                            },
                            {
                                "time_epoch": 1660143600,
                                "time": "2022-08-10 18:00",
                                "temp_c": 33.0,
                                "temp_f": 91.4,
                            },
                            {
                                "time_epoch": 1660147200,
                                "time": "2022-08-10 19:00",
                                "temp_c": 30.7,
                                "temp_f": 87.3,
                            },
                            {
                                "time_epoch": 1660150800,
                                "time": "2022-08-10 20:00",
                                "temp_c": 28.5,
                                "temp_f": 83.2,
                            },
                            {
                                "time_epoch": 1660154400,
                                "time": "2022-08-10 21:00",
                                "temp_c": 26.2,
                                "temp_f": 79.2,
                            },
                            {
                                "time_epoch": 1660158000,
                                "time": "2022-08-10 22:00",
                                "temp_c": 26.0,
                                "temp_f": 78.8,
                            },
                            {
                                "time_epoch": 1660161600,
                                "time": "2022-08-10 23:00",
                                "temp_c": 25.8,
                                "temp_f": 78.4,
                            }
                        ]
                    },
                    {
                        "date": "2022-08-11",
                        "date_epoch": 1660176000,
                        "day": {
                            "maxtemp_c": 36.1,
                            "maxtemp_f": 97.0,
                            "mintemp_c": 23.0,
                            "mintemp_f": 73.4,
                            "avgtemp_c": 31.3,
                            "avgtemp_f": 88.3,
                        },
                        "hour": [
                            {
                                "time_epoch": 1660165200,
                                "time": "2022-08-11 00:00",
                                "temp_c": 25.6,
                                "temp_f": 78.1,
                            },
                            {
                                "time_epoch": 1660168800,
                                "time": "2022-08-11 01:00",
                                "temp_c": 25.2,
                                "temp_f": 77.3,
                            },
                            {
                                "time_epoch": 1660172400,
                                "time": "2022-08-11 02:00",
                                "temp_c": 24.7,
                                "temp_f": 76.5,
                            },
                            {
                                "time_epoch": 1660176000,
                                "time": "2022-08-11 03:00",
                                "temp_c": 24.3,
                                "temp_f": 75.7,
                            },
                            {
                                "time_epoch": 1660179600,
                                "time": "2022-08-11 04:00",
                                "temp_c": 23.9,
                                "temp_f": 75.0,
                            },
                            {
                                "time_epoch": 1660183200,
                                "time": "2022-08-11 05:00",
                                "temp_c": 23.4,
                                "temp_f": 74.2,
                            },
                            {
                                "time_epoch": 1660186800,
                                "time": "2022-08-11 06:00",
                                "temp_c": 23.0,
                                "temp_f": 73.4,
                            },
                            {
                                "time_epoch": 1660190400,
                                "time": "2022-08-11 07:00",
                                "temp_c": 25.1,
                                "temp_f": 77.2,
                            },
                            {
                                "time_epoch": 1660194000,
                                "time": "2022-08-11 08:00",
                                "temp_c": 27.3,
                                "temp_f": 81.1,
                            },
                            {
                                "time_epoch": 1660197600,
                                "time": "2022-08-11 09:00",
                                "temp_c": 29.4,
                                "temp_f": 84.9,
                            },
                            {
                                "time_epoch": 1660201200,
                                "time": "2022-08-11 10:00",
                                "temp_c": 31.4,
                                "temp_f": 88.6,
                            },
                            {
                                "time_epoch": 1660204800,
                                "time": "2022-08-11 11:00",
                                "temp_c": 33.5,
                                "temp_f": 92.2,
                            },
                            {
                                "time_epoch": 1660208400,
                                "time": "2022-08-11 12:00",
                                "temp_c": 35.5,
                                "temp_f": 95.9,
                            },
                            {
                                "time_epoch": 1660212000,
                                "time": "2022-08-11 13:00",
                                "temp_c": 35.7,
                                "temp_f": 96.3,
                            },
                            {
                                "time_epoch": 1660215600,
                                "time": "2022-08-11 14:00",
                                "temp_c": 35.9,
                                "temp_f": 96.6,
                            },
                            {
                                "time_epoch": 1660219200,
                                "time": "2022-08-11 15:00",
                                "temp_c": 36.1,
                                "temp_f": 97.0,
                            },
                            {
                                "time_epoch": 1660222800,
                                "time": "2022-08-11 16:00",
                                "temp_c": 34.9,
                                "temp_f": 94.8,
                            },
                            {
                                "time_epoch": 1660226400,
                                "time": "2022-08-11 17:00",
                                "temp_c": 33.6,
                                "temp_f": 92.5,
                            },
                            {
                                "time_epoch": 1660230000,
                                "time": "2022-08-11 18:00",
                                "temp_c": 32.4,
                                "temp_f": 90.3,
                            },
                            {
                                "time_epoch": 1660233600,
                                "time": "2022-08-11 19:00",
                                "temp_c": 30.2,
                                "temp_f": 86.3,
                            },
                            {
                                "time_epoch": 1660237200,
                                "time": "2022-08-11 20:00",
                                "temp_c": 27.9,
                                "temp_f": 82.3,
                            },
                            {
                                "time_epoch": 1660240800,
                                "time": "2022-08-11 21:00",
                                "temp_c": 25.7,
                                "temp_f": 78.3,
                            },
                            {
                                "time_epoch": 1660244400,
                                "time": "2022-08-11 22:00",
                                "temp_c": 25.1,
                                "temp_f": 77.2,
                            },
                            {
                                "time_epoch": 1660248000,
                                "time": "2022-08-11 23:00",
                                "temp_c": 24.6,
                                "temp_f": 76.2,
                            }
                        ]
                    }
                ]
            }
        }
