from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

USERNAME = "email"
PASSWORD = "password"

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0"
service = Service("Y:\Python Projects\development\drivers\geckodriver.exe")

# allow geolocation on firefox
options = webdriver.FirefoxOptions()
options.preferences["permissions.default.geo"] = 1

driver = webdriver.Firefox(service=service, options=options)

driver.get("https://tinder.com/")
driver.maximize_window()

# set parent window
base_window = driver.window_handles[0]
time.sleep(1)

login = driver.find_element(By.CSS_SELECTOR, '''a[href="https://tinder.onelink.me/9K8a/3d4abb81"''')
login.click()
time.sleep(3)

google_login = driver.find_element(By.CSS_SELECTOR, '''button[aria-label="Log in with Google"]''')
google_login.click()
time.sleep(2)

# switch to popup window
google_popup = driver.window_handles[1]
driver.switch_to.window(google_popup)
print(driver.title)

# username = driver.find_element(By.CSS_SELECTOR, '''input[aria-label="Email or phone"''')
username = driver.find_element(By.XPATH, '''//input[@type='email']''')
username.send_keys(USERNAME)

next = driver.find_element(By.XPATH, '''//span[text()='Next']''')
next.click()
time.sleep(2)
password = driver.find_element(By.XPATH, '''//input[@type='password']''')
password.send_keys(PASSWORD)
next_2 = driver.find_element(By.XPATH, '''//span[text()='Next']''')
next_2.click()

# switch back to parent window
driver.switch_to.window(base_window)
print(driver.title)
time.sleep(3)

# allow locations
location_allow = driver.find_element(By.XPATH, '''//span[text()='Allow']''')
location_allow.click()

# not interested in notifications
notification = driver.find_element(By.XPATH, '''//span[text()='Not interested']''')
notification.click()

# accept cookies
cookies = driver.find_element(By.XPATH, '''//span[text()='I accept']''')
cookies.click()
time.sleep(2)

# automation
for n in range(100):
    time.sleep(1)
    try:
        driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.ARROW_RIGHT)

    except NoSuchElementException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()
        except NoSuchElementException:
            time.sleep(1)

# driver.quit()
