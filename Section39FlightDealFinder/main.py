#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager

flight_search_api = FlightSearch()
data_manager_api = DataManager()
notification_manager = NotificationManager("pfvatterott@gmail.com")


row_data = data_manager_api.get_rows()
for row in row_data:
    iata_code = ""
    if row['iataCode'] == '':
        iata_code = flight_search_api.get_city_code(row['city'])
        data_manager_api.update_iata_code(row_id=row['id'], iataCode=iataCode)
    else:
        iata_code = row['iataCode']
    flight_data = flight_search_api.get_flight_data(fly_from='SLC', fly_to=iata_code)
    if row['lowestPrice'] > flight_data['data'][0]['price']:
        data_manager_api.update_lowest_price(row_id=row['id'], lowest_price=flight_data['data'][0]['price'])
        text = f"Low price alert! Only ${flight_data['data'][0]['price']} to fly from {flight_data['data'][0]['cityFrom']}-{flight_data['data'][0]['flyFrom']} to {flight_data['data'][0]['cityTo']}-{flight_data['data'][0]['flyTo']} on {flight_data['data'][0]['local_departure'].split('T')[0]}"
        
        notification_manager.send_email(text=text)
        