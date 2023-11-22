from decouple import config
import datetime
import requests

kiwi_apiToken = config("kiwi_apiToken")

class FlightSearch:
    def __init__(self):
        self.tomorrow = (datetime.date.today() + datetime.timedelta(days=1)).strftime('%d/%m/%Y')
        self.six_months_from_now = (datetime.date.today() + datetime.timedelta(days=180)).strftime('%d/%m/%Y')
        self.currency = "USD"
        
        
    def get_city_code(self, search_term):
        parameters = {
            "term": search_term,
            "location_types": "city"
        }
        headers = {
            "apikey": kiwi_apiToken
        }
        city_response = requests.get("https://api.tequila.kiwi.com/locations/query", params=parameters, headers=headers) 
        city_response.raise_for_status()
        city_data = city_response.json()
        return city_data['locations'][0]['code']
    
        
    def get_flight_data(self, fly_from, fly_to):
        parameters = {
            "fly_from": f"city:{fly_from}",
            "fly_to": f"city:{fly_to}",
            "curr": self.currency,
            "date_from": self.tomorrow,
            "date_to": self.six_months_from_now,
            "limit": 1,
            "sort": "price"
        }
        headers = {
            "apikey": kiwi_apiToken
        }
        flight_response = requests.get("https://api.tequila.kiwi.com/v2/search", params=parameters, headers=headers) 
        flight_response.raise_for_status()
        flight_data = flight_response.json()
        return flight_data