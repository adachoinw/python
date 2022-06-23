import requests
from flight_data import FlightData

QUERY_API = "https://tequila-api.kiwi.com/locations/query"
SEARCH_API = "https://tequila-api.kiwi.com/v2/search"

API_KEY = "<kiwi api key>"


class FlightSearch:

    def search(self, city_name):
        """Location query: gets the IATA Code of the city"""
        header = {
            "apikey": API_KEY
        }

        search_config = {
            "term": city_name,
            "location_types": "city"
        }

        response = requests.get(url=QUERY_API, params=search_config, headers=header)
        return response.json()["locations"][0]["code"]

    def find_flights(self, from_city, to_city, from_time, to_time):

        header = {
            "apikey": API_KEY
        }

        search_params = {
            "fly_from": f"city:{from_city}",
            "fly_to": f"city:{to_city}",
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "max_stopovers": 0,
            "flight_type": "round",
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "curr": "GBP"
        }

        response = requests.get(url=SEARCH_API, params=search_params, headers=header)

        try:
            data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {to_city}.")
            return None

        flight_data = FlightData(
            price=data["price"],
            origin_city=data["route"][0]["cityFrom"],
            origin_airport=data["route"][0]["flyFrom"],
            destination_city=data["route"][0]["cityTo"],
            destination_airport=data["route"][0]["flyTo"],
            out_date=data["route"][0]["local_departure"].split("T")[0],
            return_date=data["route"][1]["local_departure"].split("T")[0]
        )
        print(f"{flight_data.destination_city}: ${flight_data.price}")
        return flight_data