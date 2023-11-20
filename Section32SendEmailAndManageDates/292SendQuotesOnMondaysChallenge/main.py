import smtplib
import datetime as dt
import random
from decouple import config

my_email = "pfvatterott@gmail.com"
password = config('gmail_password')

def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs="paul.vatterott@yahoo.com", 
            msg=f"Subject:Monday Motivation\n\n{get_quote()}"
        )

def get_quote():
    quote_list = []
    with open("Section32SendEmailAndManageDates\\292SendQuotesOnMondaysChallenge\quotes.txt") as file:
        quote_list = file.readlines()
    return random.choice(quote_list)

now = dt.datetime.now()
day_of_week = now.weekday()
if day_of_week == 0:
    send_email()