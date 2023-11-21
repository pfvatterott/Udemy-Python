from twilio.rest import Client
from decouple import config
import requests

weather_api_key = config("weather_api_key")
MY_LAT = 40.760780
MY_LONG = -111.891045
twilio_account_id = config("twilio_account_id")
twilio_auth_token = config("twilio_auth_token")
twilio_number = config("twilio_phone_number")



parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": weather_api_key,
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
        



client = Client(twilio_account_id, twilio_auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_=twilio_number,
                     to='+1 651 308 4855'
                 )
print(message.status)

