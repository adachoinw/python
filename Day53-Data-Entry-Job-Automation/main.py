import json
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

CHROME_DRIVER_PATH = "Y:\Python Projects\development\drivers\chromedriver.exe"
URL = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
google_form = "https://forms.gle/RhaJKg2vabFt13em6"

# use http://myhttpheader.com/ to check
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,zh-TW;q=0.8,zh;q=0.7"
}

response = requests.get(URL, headers=headers)
webpage = response.text
# print(webpage)

soup = BeautifulSoup(webpage, "html.parser")

data = json.loads(soup.select_one("script[data-zrr-shared-data-key]").contents[0].strip("!<>-"))
all_data = data["cat1"]["searchResults"]["listResults"]

link_list = []
price_list = []
address_list = []

for i in range(len(all_data)):
    # print(all_data[i])
    if "https" not in all_data[i]["detailUrl"]:
        full_link = f"https://www.zillow.com{all_data[i]['detailUrl']}"
        link_list.append(full_link)
    try:
        price = all_data[i]["price"]
    except KeyError:
        price = all_data[i]["units"][0]["price"]
    price_list.append(price)

    address = all_data[i]["address"]
    address_list.append(address)

new_price_list = []
for price in price_list:
    new_price_list.append(price[:6])

print(link_list)
print(new_price_list)
print(address_list)

service = Service(CHROME_DRIVER_PATH)
driver = webdriver.Chrome(service=service)

for i in range(len(link_list)):
    driver.get(google_form)
    driver.maximize_window()
    time.sleep(1)

    property_address = driver.find_element(By.CSS_SELECTOR, "div.Xb9hP input")
    property_address.send_keys(address_list[i])

    monthly_price = driver.find_element(By.XPATH,
                                        '''//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input''')
    monthly_price.send_keys(new_price_list[i])

    property_link = driver.find_element(By.XPATH,
                                        '''//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input''')
    property_link.send_keys(link_list[i])

    submit_button = driver.find_element(By.XPATH, "//span[text()='Submit']")
    submit_button.click()
    time.sleep(1)
