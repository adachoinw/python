from selenium import webdriver
from selenium.common import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

CHROME_DRIVER_PATH = "Y:\Python Projects\development\drivers\chromedriver.exe"
SIMILAR_ACCOUNT = "chefsteps"
USERNAME = "igname"
PASSWORD = "password"

service = Service(CHROME_DRIVER_PATH)


class InstaFollower:
    def __init__(self, chrome_service):
        self.driver = webdriver.Chrome(service=chrome_service)


    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        self.driver.maximize_window()
        time.sleep(4)
        username = self.driver.find_element(By.XPATH, "//input[@name='username']")
        username.send_keys(USERNAME)
        password = self.driver.find_element(By.XPATH, "//input[@name='password']")
        password.send_keys(PASSWORD, Keys.ENTER)
        time.sleep(3)
        not_now_button = self.driver.find_element(By.CSS_SELECTOR, "button[class='_acan _acao _acas']")
        not_now_button.click()
        time.sleep(3)
        notification = self.driver.find_element(By.CSS_SELECTOR, "button[class='_a9-- _a9_1']")
        notification.click()


    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers/")
        time.sleep(3)
        followers_amt = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/section/main/div/header/section/ul/li[2]/a/div/span")
        num_of_followers = int(followers_amt.text.strip("K")) * 1000
        scroll = self.driver.find_element(By.CLASS_NAME, "_aano")
        for i in range(num_of_followers):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll)
            time.sleep(1)


    def follow(self):
        follow_buttons = self.driver.find_elements(By.CSS_SELECTOR, "._aano button")
        for button in follow_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")
                cancel_button.click()



insta_bot = InstaFollower(service)
insta_bot.login()
insta_bot.find_followers()
insta_bot.follow()
