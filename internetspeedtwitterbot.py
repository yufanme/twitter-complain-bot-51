from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import random


CHROME_DRIVER_PATH = "/Users/WilliamYu/Development/chromedriver"
TWITTER_NAME = os.environ["TWITTER_NAME"]
TWITTER_PASSWORD = os.environ["TWITTER_PASSWORD"]
PROMISE_DOWN = 500
PROMISE_UP = 30


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(CHROME_DRIVER_PATH))
        self.down = 0
        self.up = 0
        self.promise_down = PROMISE_DOWN
        self.promise_up = PROMISE_UP

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        go_button = self.driver.find_element(By.CSS_SELECTOR, ".start-text")
        go_button.click()
        # time.sleep(180)
        print("already sleep 180s.")
        # click esc on the main page.
        body = self.driver.find_element(By.XPATH, "//body")
        body.send_keys(Keys.ESCAPE)
        # get download and upload information.
        # self.down = float(self.driver.find_element(By.CSS_SELECTOR, ".download-speed").text)
        # self.up = float(self.driver.find_element(By.CSS_SELECTOR, ".upload-speed").text)
        self.down = 1
        self.up = 1
        print(f"down: {self.down}")
        print(f"up: {self.up}")

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/")

        time.sleep(5)
        sign_in_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a/div/span/span')
        sign_in_button.click()

        time.sleep(2)
        user_inbox = self.driver.find_element(By.NAME, 'text')
        user_inbox.send_keys(TWITTER_NAME)
        time.sleep(random.uniform(1, 2))
        user_inbox.send_keys(Keys.ENTER)

        time.sleep(random.uniform(1, 2))

        password_inbox = self.driver.find_element(By.NAME, 'password')
        password_inbox.send_keys(TWITTER_PASSWORD)
        time.sleep(random.uniform(1, 2))
        password_inbox.send_keys(Keys.ENTER)

        time.sleep(random.uniform(1, 2))

        if self.promise_down < self.down or self.promise_up < self.up:
            complain_text = f"Hi, Internet provider, why is my internet speed {self.down}/down/{self.up}up " \
                            f"when I pay for {self.promise_down}down/{self.promise_up}up?"
            tweet_inbox = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/label/div[1]/div/div/div/div/div/div/div/div/div/span/span')
            tweet_inbox.send_keys(complain_text)
            time.sleep(random.uniform(1, 2))
            tweet_button = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span')
            tweet_button.click()



