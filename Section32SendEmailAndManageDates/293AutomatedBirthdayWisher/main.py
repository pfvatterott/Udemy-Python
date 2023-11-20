import smtplib
import datetime as dt
import random
import pandas
from decouple import config

my_email = "pfvatterott@gmail.com"
password = config('gmail_password')

def send_email(email, text):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email, 
            to_addrs=email, 
            msg=f"Subject:Happy Birthday!\n\n{text}"
        )

def get_letter(name):
    letter_number = random.randint(1, 3)
    with open(f"Section32SendEmailAndManageDates\\293AutomatedBirthdayWisher\letter_templates\letter_{letter_number}.txt") as file:
        letter = file.readlines()
    letter = "".join(letter)
    letter = letter.replace("[NAME]", name)
    return letter
    
get_letter("Paul")

csv_data = pandas.read_csv("Section32SendEmailAndManageDates\\293AutomatedBirthdayWisher\\birthdays.csv")
birthday_data = csv_data.to_dict(orient="records")

now = dt.datetime.now()
year = now.year
month = now.month
day = now.day

for birthday in birthday_data:
    if birthday["month"] == month and birthday["day"] == day:
        letter = get_letter(birthday["name"])
        send_email(birthday["email"], letter)





