import requests
from bs4 import BeautifulSoup
from decouple import config
import smtplib
password = config('gmail_password')

def send_email(item_url, price):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user='pfvatterott@gmail.com', password=password)
            connection.sendmail(
                from_addr='pfvatterott@gmail.com', 
                to_addrs='pfvatterott@gmail.com', 
                msg=f"Subject:Price Drop!\n\nThe item you were looking at just fell to a low price of ${price}!\nLink: {item_url}"
            )

amazon_url = "https://www.amazon.com/dp/B01NBKTPTS?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9"
    
}
amazon_response = requests.get(url=amazon_url, headers=headers)
amazon_soup = BeautifulSoup(amazon_response.text, 'html.parser')
cost_elem = amazon_soup.select_one(selector=".aok-offscreen")
cost = float(cost_elem.getText().split("$")[1].split(" ")[0])
if cost < 100:
    send_email(amazon_url, cost)