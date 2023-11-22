import time
from flight_search import FlightSearch
from data_manager import DataManager
from notification_manager import NotificationManager
from flight_data import FlightData

flight_search_api = FlightSearch()
data_manager_api = DataManager()
notification_manager = NotificationManager("pfvatterott@gmail.com")
flight_data_manager = FlightData()

print("Welcome to Paul's Flight Club.\nWe find the best flight deals and email you.")
create_user = input("Do you want to create a new profile? (y/n)\n")
if create_user.lower() == 'y':
    first_name = input("What is your first name?\n")
    last_name = input("What is your last name?\n")
    email = input("What is your email?\n")
    data_manager_api.add_user_row(first_name=first_name, last_name=last_name, email=email)


def sync_users_check_flights():
    flight_data_manager.sync_data()
    flight_data_manager.check_deals()

while True:
    print("test")
    sync_users_check_flights()
    time.sleep(60)