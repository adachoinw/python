from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("Y:\Python Projects\development\chrome_driver\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.python.org/")
driver.maximize_window() #maximizes window when open, so it can scrape the year

datetime = driver.find_elements(By.CSS_SELECTOR, ".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget li a")
events = {}

for n in range(len(datetime)):
    events[n] = {
        "time": datetime[n].text,
        "name": event_names[n].text
    }

print(events)
driver.quit()
