import requests
from decouple import config
sheety_flight_token = config("sheety_flight_token")

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.prices_url = "https://api.sheety.co/efbdef51c73a42ea2256a45219e84905/flightDeals (pythonUdemy)/prices"
        self.users_url = "https://api.sheety.co/efbdef51c73a42ea2256a45219e84905/flightDeals (pythonUdemy)/users"
        
    def get_prices_url(self):
        sheet_headers = {
            "Authorization": f"Bearer {sheety_flight_token}"
        }
        get_rows_response = requests.get(url=self.prices_url, headers=sheet_headers)
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
        update_row_response = requests.put(url=f"{self.prices_url}/{row_id}", json=update_row_params, headers=sheet_headers)
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
        update_row_response = requests.put(url=f"{self.prices_url}/{row_id}", json=update_row_params, headers=sheet_headers)
        update_row_response.raise_for_status()
        return update_row_response
    
    def get_users_rows(self):
        sheet_headers = {
            "Authorization": f"Bearer {sheety_flight_token}"
        }
        get_rows_response = requests.get(url=self.users_url, headers=sheet_headers)
        get_rows_response.raise_for_status()
        rows_data = get_rows_response.json()
        return rows_data['users']
    
    def add_user_row(self, first_name, last_name, email):
        add_user_params = {
            "user": {
                'firstName': first_name,
                'lastName': last_name,
                'email': email
            }
        }
        sheet_headers = {
            "Authorization": f"Bearer {sheety_flight_token}"
        }
        add_user_response = requests.post(url=self.users_url, json=add_user_params, headers=sheet_headers)
        add_user_response.raise_for_status()
        return add_user_response