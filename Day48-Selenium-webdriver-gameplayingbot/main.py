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
            if item.get_attribute("class") != "grayed":
                item_ids.append(item)
        item_ids[-1].click()
        timeout_five_sec = time.time() + 5

    if time.time() > five_min:
        cps = driver.find_element(By.ID, "cps").text
        print(cps)









# all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
# item_prices = []
# for price_element in all_prices:
#     price = price_element.text
#     if price != "":
#         cost = int(price.split("-")[1].replace(",", ""))
#         item_prices.append(cost)
# print(item_prices)
#
# cookie_upgrades = {}
# for n in range(len(item_prices)):
#     cookie_upgrades[item_prices[n]] = item_ids[n]
#
#
# money_element = driver.find_element(By.ID, "money").text
# if "," in money_element:
#     money_element.replace(",", "")
# money = int(money_element)

    #
    #
    # cursor_element = driver.find_element(By.ID, "buyCursor")
    # cursor_price = int(cursor_element.text)
    # cursor_element.click()
    #
    # grandma = driver.find_element(By.ID, "buyGrandma")
    # grandma_price = grandma.text
    # grandma.click()
    #
    # factory = driver.find_element(By.ID, "buyFactory")
    # factory_price = factory.text
    # factory.click()
    #
    # mine = driver.find_element(By.ID, "buyMine")
    # mine.click()
    #
    # shipment = driver.find_element(By.ID, "buyShipment")
    # shipment.click()
    #
    # alchemy_lab = driver.find_element(By.ID, "buyAlchemy lab")
    # alchemy_lab.click()
    #
    # portal = driver.find_element(By.ID, "buyPortal")
    # portal.click()
    #
    # time_machine = driver.find_element(By.ID, "buyTime machine")
    # time_machine.click()

# driver.close() # closes the active tab
# driver.quit() #closes all tabs
