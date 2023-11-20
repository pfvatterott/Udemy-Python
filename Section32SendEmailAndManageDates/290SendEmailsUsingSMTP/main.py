import smtplib
from decouple import config

my_email = "pfvatterott@gmail.com"
password = config('gmail_password')

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email, 
        to_addrs="paul.vatterott@yahoo.com", 
        msg="Subject:Hello\n\nThis is the body of the email"
    )