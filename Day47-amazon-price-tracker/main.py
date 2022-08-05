import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

my_email = "email@gmail.com"
password = "fitodiavmicqjrmo"

URL = "https://www.amazon.com/dp/B08L3SW8DZ/ref=sbl_dpx_kitchen-electric-cookware_B08GC6PL3D_0"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0",
    "Accept-Language": "en-US,en;q=0.5",
}

response = requests.get(URL, headers=headers)
webpage = response.text
# print(webpage)

soup = BeautifulSoup(webpage, "lxml")
# print(soup.prettify())

price = soup.find_all(name="span", class_="a-offscreen")[0].getText()
price_without_currency = price.split("$")[1]
price_float = float(price_without_currency)
print(price_float)

if price_float < 200:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=my_email,
                            msg=f"Subject:Amazon Price Alert!\n\nThe price of the product is ${price_float} now!")