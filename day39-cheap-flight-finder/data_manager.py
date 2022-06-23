import requests

SHEET_GET_API = "https://api.sheety.co/f7e201f9294aa3992a0dc1215e6e4ac7/flightDeals/prices"
sheet_bearer = {
    "Authorization": "Bearer <bearertoken>"
}

class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        """Gets data from Google sheet"""
        sheet_get_response = requests.get(url=SHEET_GET_API, headers=sheet_bearer)
        self.destination_data = sheet_get_response.json()["prices"]
        return self.destination_data

    def update_destination_data(self):
        """Puts IATA codes into Google Sheet"""
        for city in self.destination_data:
            sheet_put_config = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            sheet_put_response = requests.put(url=f"{SHEET_GET_API}/{city['id']}", json=sheet_put_config,
                                              headers=sheet_bearer)
            print(sheet_put_response.text)
