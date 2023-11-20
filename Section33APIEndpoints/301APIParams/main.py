import requests
import datetime as dt
MY_LAT = 40.760780
MY_LONG = -111.891045

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# data = response.json()
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]

# iss_position = (longitude, latitude)
# print(iss_position)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

sunrise_sunset_response = requests.get("https://api.sunrise-sunset.org/json", params=parameters) 
sunrise_sunset_response.raise_for_status()
sunrise_sunset_data = sunrise_sunset_response.json()

sunrise = sunrise_sunset_data["results"]["sunrise"]
sunset = sunrise_sunset_data["results"]["sunset"]
sunrise = sunrise.split("T")[1].split(":")[0]
sunset = sunset.split("T")[1].split(":")[0]


time_now = dt.datetime.now()
time_now.hour
