import requests
import smtplib
import time
from decouple import config
from datetime import datetime

MY_LAT = 40.760780
MY_LONG = -111.891045

my_email = "pfvatterott@gmail.com"
password = config('gmail_password')

def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs="paul.vatterott@yahoo.com", 
            msg=f"Subject:ISS Notification\n\nLook Up! The ISS is in the sky."
        )


while True:
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now()

    if (iss_latitude > (MY_LAT - 5) or iss_latitude < (MY_LAT + 5)) and (iss_longitude > (MY_LONG - 5) or iss_longitude < (MY_LONG + 5)) and (time_now.hour < sunrise) and (time_now.hour > sunset):
        send_email()
    
    
    time.sleep(60)
