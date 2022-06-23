from data_manager import DataManager
from notification_manager import NotificationManager
from flight_search import FlightSearch
from datetime import datetime, timedelta

data_manager = DataManager()
flight_search = FlightSearch()
notification_manager = NotificationManager()
sheet_data = data_manager.get_destination_data()
# pprint(sheet_data)

ORIGIN_CITY_IATA = "LON"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.search(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_data()

tomorrow = (datetime.now() + timedelta(days=1))
to_date = (datetime.now() + timedelta(days=6 * 30))

for destination in sheet_data:
    flight = flight_search.find_flights(ORIGIN_CITY_IATA, destination["iataCode"], tomorrow, to_date)

    if flight is not None and flight.price < destination["lowestPrice"]:
        try:
            notification_manager.send_sms(
                f"Low price alert! Fly from {flight.origin_airport} to {flight.destination_airport}"
                f" is only {flight.price} from {flight.out_date} to {flight.return_date}.")
        except AttributeError:
            None

