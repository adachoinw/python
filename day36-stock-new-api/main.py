import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "stockapikey"
NEWS_APIKEY = "newsapikey"

ACCOUNT_SID = "account_sid"
AUTH_TOKEN = "auth_token"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "interval": "5min",
    "apikey": STOCK_API_KEY

}
response = requests.get(STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
stock_data = response.json()["Time Series (Daily)"]
stock_data_list = [value for (key, value) in stock_data.items()]
yst_data = stock_data_list[0]
yst_close_price = yst_data["4. close"]
print(yst_close_price)


day_before_data = stock_data_list[1]
day_before_close_price = day_before_data["4. close"]
print(day_before_close_price)

difference = abs(float(yst_close_price) - float(day_before_close_price))
print(difference)

diff_percent = (difference / float(yst_close_price)) * 100
print(diff_percent)

if diff_percent > 5:
    news_param = {
        "apiKey": NEWS_APIKEY,
        "qInTitle": COMPANY_NAME
    }

    news_response = requests.get(NEWS_ENDPOINT, params=news_param)
    articles = news_response.json()["articles"]
    three_articles = articles[:3]

    print(three_articles[0])
    headlines = [f"Headline: {article['title']}.\nBrief: {article['description']}" for article in three_articles]
    print(headlines)

    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    for article in headlines:
        message = client.messages.create(
            body=article,
            from_="+1234567890",
            to="+1234567890",
        )
