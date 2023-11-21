from decouple import config
import requests

api_key = config("weather_api_key")
MY_LAT = 40.760780
MY_LONG = -111.891045



parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

weather_response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters) 
weather_response.raise_for_status()
weather_data = weather_response.json()
hourly_weather = weather_data["hourly"]

gonna_rain = False
for hour in range(0, 12):
    if hourly_weather[hour]["weather"][0]["id"] < 700:
        gonna_rain = True

if gonna_rain:
    print("It gonna rain")
        


