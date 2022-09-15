from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

PROMISED_DOWN = 500
PROMISED_UP = 500
CHROME_DRIVER_PATH = "Y:\Python Projects\development\drivers\chromedriver.exe"
TWITTER_EMAIL = "EMAIL"
TWITTER_PASSWORD = "PASSWORD"
TWITTER_USERNAME = "USERNAME"

service = Service(CHROME_DRIVER_PATH)


class InternetSpeedTwitterBot:
    def __init__(self, chrome_service):
        self.driver = webdriver.Chrome(service=chrome_service)
        time.sleep(1)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net")
        self.driver.maximize_window()
        go_button = self.driver.find_element(By.XPATH, "//span[text()='Go']")
        go_button.click()
        print("Testing speed...")
        time.sleep(60)
        self.down = float(self.driver.find_element(By.XPATH,
                                                   "//span[@class='result-data-large number result-data-value download-speed']").text)
        self.up = float(self.driver.find_element(By.XPATH,
                                                 "//span[@class='result-data-large number result-data-value upload-speed']").text)
        print(f"Down: {self.down}Mbps")
        print(f"Up: {self.up}Mbps")

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/")
        self.driver.maximize_window()
        print("Posting tweet...")
        time.sleep(2)

        sign_in = self.driver.find_element(By.XPATH, "//span[text()='Sign in']")
        sign_in.click()
        time.sleep(2)

        email = self.driver.find_element(By.XPATH, "//input[@autocomplete='username']")
        email.send_keys(TWITTER_EMAIL)

        next_button = self.driver.find_element(By.XPATH, "//span[text()='Next']")
        next_button.click()
        time.sleep(2)

        try:
            unusual_activity = self.driver.find_element(By.XPATH,
                                               "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input")
            unusual_activity.send_keys(TWITTER_USERNAME)
            unusual_next = self.driver.find_element(By.XPATH,
                                                    "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div")
            unusual_next.click()
            time.sleep(2)

        except NoSuchElementException:
            print("No need to verify")

        password = self.driver.find_element(By.XPATH, "//input[@name='password']")
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)
        time.sleep(5)

        tweet_compose = self.driver.find_element(By.CLASS_NAME, "public-DraftStyleDefault-block")
        tweet_compose.send_keys(
            f"Hey @Bell, why is my internet speed {self.down}Mbps down/{self.up}Mbps up when I pay for 500Mbps "
            f"down/500Mbps up?")

        tweet_click = self.driver.find_element(By.XPATH,
                                               '''//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]''')
        tweet_click.click()
        print("Tweet posted.")
        time.sleep(2)


bot = InternetSpeedTwitterBot(service)
bot.get_internet_speed()

if bot.down < PROMISED_DOWN or bot.up < PROMISED_UP:
    print("Speed is slower than promised.")
    bot.tweet_at_provider()
    bot.driver.quit()
else:
    print("Speed is good today.")
    bot.driver.quit()
