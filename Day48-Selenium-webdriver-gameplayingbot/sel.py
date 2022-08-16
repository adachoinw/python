from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service("Y:\Python Projects\development\chrome_driver\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("http://orteil.dashnet.org/experiments/cookie/")
# driver.maximize_window()

cookie = driver.find_element(By.ID, "cookie")

timeout_five_sec = time.time() + 5
five_min = time.time() + 60 * 5

while True:
    cookie.click()

    if time.time() > timeout_five_sec:

        items_to_buy = driver.find_elements(By.CSS_SELECTOR, "#store div")
        item_ids = []
        for item in items_to_buy:
            item_id = item.get_attribute("id")
            if item_id != "" and item.get_attribute("class") != "grayed":
                item_ids.append(item_id)
        print(item_ids)

        item_cost = driver.find_elements(By.CSS_SELECTOR, "#store b")
        item_prices = []
        for price in item_cost:
            item_price = price.text
            if item_price != "":
                cost = int(item_price.split("-")[1].replace(",", ""))
                item_prices.append(cost)
        print(item_prices)

        cookie_upgrades = {}
        for n in range(len(item_ids)):
            cookie_upgrades[item_prices[n]] = item_ids[n]
        print(cookie_upgrades)

        money_element = driver.find_element(By.ID, "money").text
        if "," in money_element:
            money_element.replace(",", "")
        money = int(money_element)

        affordable_upgrades = {}
        for cost, item_id in cookie_upgrades.items():
            if money > cost:
                affordable_upgrades[cost] = item_id

        highest_affordable_item = max(affordable_upgrades)
        driver.find_element(By.ID, affordable_upgrades[highest_affordable_item]).click()

        timeout_five_sec = time.time() + 5

    if time.time() > five_min:
        cps = driver.find_element(By.ID, "cps")
        print(cps)
