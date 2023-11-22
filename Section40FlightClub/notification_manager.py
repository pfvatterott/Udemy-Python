import smtplib
from decouple import config

password = config('gmail_password')

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def __init__(self, receiver_email):
        self.sender_email = "pfvatterott@gmail.com"
        
        
    def send_email(self, text, to_address):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.sender_email, password=password)
            connection.sendmail(
                from_addr=self.sender_email, 
                to_addrs=to_address, 
                msg=f"Subject:Flight Price Alert!\n\n{text}"
            )