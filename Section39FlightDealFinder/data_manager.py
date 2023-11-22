import requests
from decouple import config
sheety_flight_token = config("sheety_flight_token")

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.url = "https://api.sheety.co/efbdef51c73a42ea2256a45219e84905/flightDeals (pythonUdemy)/prices"
        
    def get_rows(self):
        sheet_headers = {
            "Authorization": f"Bearer {sheety_flight_token}"
        }
        get_rows_response = requests.get(url=self.url, headers=sheet_headers)
        get_rows_response.raise_for_status()
        rows_data = get_rows_response.json()
        return rows_data['prices']
    
    def update_iata_code(self, row_id, iataCode):
        update_row_params = {
            "price": {
                'iataCode': iataCode
            }
        }
        sheet_headers = {
            "Authorization": f"Bearer {sheety_flight_token}"
        }
        update_row_response = requests.put(url=f"{self.url}/{row_id}", json=update_row_params, headers=sheet_headers)
        update_row_response.raise_for_status()
        return update_row_response
    
    def update_lowest_price(self, row_id, lowest_price):
        update_row_params = {
            "price": {
                'lowestPrice': lowest_price
            }
        }
        sheet_headers = {
            "Authorization": f"Bearer {sheety_flight_token}"
        }
        update_row_response = requests.put(url=f"{self.url}/{row_id}", json=update_row_params, headers=sheet_headers)
        update_row_response.raise_for_status()
        return update_row_response