from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

USERNAME = "email"
PASSWORD = "pw"

service = Service("Y:\Python Projects\development\chrome_driver\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3143872993&f_AL=true&f_WT=2&geoId=101174742&keywords"
           "=devops&location=Canada&refresh=true")
driver.maximize_window()

time.sleep(2)

try:
    sign_in_word = driver.find_element(By.XPATH, '''//*[@id="main-content"]/div/form/p/button''').click()
    username = driver.find_element(By.CSS_SELECTOR, '''input[autocomplete="username"]''')
    username.send_keys(USERNAME)
    password = driver.find_element(By.ID, "session_password")
    password.send_keys(PASSWORD)
    password.send_keys(Keys.ENTER)
    driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3143872993&f_AL=true&f_WT=2&geoId=101174742"
               "&keywords=devops&location=Canada&refresh=true")

except NoSuchElementException:
    driver.find_element(By.CLASS_NAME, "nav__button-secondary").click()
    username = driver.find_element(By.ID, "username")
    username.send_keys(USERNAME)
    password = driver.find_element(By.ID, "password")
    password.send_keys(PASSWORD)
    password.send_keys(Keys.ENTER)

time.sleep(2)


card_container = driver.find_elements(By.CSS_SELECTOR, ".jobs-search-results__list-item")
for card in card_container:
    print("called")
    driver.execute_script("arguments[0].scrollIntoView();", card)
    card.click()
    time.sleep(2)


    try:

        easy_apply = driver.find_element(By.CLASS_NAME, "jobs-apply-button")
        easy_apply.click()

        submit_button = driver.find_element(By.CSS_SELECTOR, '''.display-flex button''')

        if submit_button.get_attribute("aria-label") == "Continue to next step":
            close_button = driver.find_element(By.CSS_SELECTOR, '''button[aria-label="Dismiss"]''')
            close_button.click()
            discard_button = driver.find_element(By.CSS_SELECTOR, '''button[data-control-name="discard_application_confirm_btn"]''')
            discard_button.click()
            print("Complex application, skipped")

        #     follow_checkbox = driver.find_element(By.ID, '''follow-company-checkbox''')
        #     driver.execute_script("arguments[0].click();", follow_checkbox)

        else:
            close_button = driver.find_element(By.CSS_SELECTOR, '''button[aria-label="Dismiss"]''')
            close_button.click()
            save_button = driver.find_element(By.CSS_SELECTOR, '''button[data-control-name="save_application_btn"]''')
            save_button.click()

    except NoSuchElementException:
        print("No application button, skipped")
        continue



