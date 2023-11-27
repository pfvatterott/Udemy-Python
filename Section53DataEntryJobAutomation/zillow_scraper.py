import requests
from bs4 import BeautifulSoup

URL = "https://appbrewery.github.io/Zillow-Clone/"


class ZillowScaper:
    def __init__(self):
        self.zillow_response = requests.get(URL)
        self.zillow_soup = BeautifulSoup(self.zillow_response.text, 'html.parser')
        self.property_list = []
        
    def getProperties(self):
        property_items = self.zillow_soup.find_all(name="li", class_="ListItem-c11n-8-84-3-StyledListCardWrapper")
        for property in property_items:
            price = property.find(name='span', class_='PropertyCardWrapper__StyledPriceLine').getText().strip()
            address = property.find(name='address').getText().strip()
            link = property.find(name='a', class_='StyledPropertyCardDataArea-anchor')['href']
            obj = {
                "price": price,
                "address": address,
                "link": link
            }
            self.property_list.append(obj)
            