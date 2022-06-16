import requests
from twilio.rest import Client
import os

api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACC_SID")
auth_token = os.environ.get("AUTH_TOKEN")

parameters = {
    "lat": 43.653225,
    "lon": -79.383186,
    "appid": api_key,
    "exclude": "current,minutely,daily"

}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Rmb to bring an umbrella",
        from_="+1234567890",
        to="+1234567890"
    )
    print(message.status)
