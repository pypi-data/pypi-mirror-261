from .base import WeatherAPIBase

import requests

class OpenMeteo(WeatherAPIBase):
    def __init__ (self, latitude, longitude, **kwargs):
        self.latitude = latitude
        self.longitude = longitude

    def get_current_temperature(self):
        payload = {"latitude":self.latitude, "longitude":self.longitude, "current":"temperature_2m"}
        result = requests.get('https://api.open-meteo.com/v1/dwd-icon', params= payload)
        result_json = result.json()
        return(result_json["current"]["temperature_2m"])

class OpenWeather(WeatherAPIBase):
    def __init__ (self, latitude, longitude, **kwargs):
        self.latitude = latitude
        self.longitude = longitude
        self.api_token = kwargs.get("api_token")

    def get_current_temperature(self):
        payload = {"lat":self.latitude, "lon":self.longitude, "appid":self.api_token}
        result = requests.get('https://api.openweathermap.org/data/2.5/weather', params= payload)
        result_json = result.json()
        return(result_json["main"]["temp"])

