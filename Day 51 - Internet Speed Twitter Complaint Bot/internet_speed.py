"""
This file implements a Internet Speed Twitter Bot Class
"""

# Import required libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# Initialize global variables
URL_TWITTER = 'https://twitter.com/'
URL_SPEEDTEST = 'https://www.speedtest.net/'
CHROME_DRIVER_PATH = 'C:/Development/chromedriver.exe'


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
        self.up = 0
        self.down = 0

    def get_internet_speed(self, url=URL_SPEEDTEST):
        """
        Gets internet speed
        :param url: Speedtest URL
        :return: Download and Upload speed
        """
        self.driver.get(url)
        self.driver.maximize_window()
        sleep(3)
        self.driver.find_element_by_css_selector('.js-start-test .start-text').click()
        sleep(60)
        down = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div['
            '2]/div/div[2]/span').text
        up = self.driver.find_element_by_xpath(
            '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div['
            '3]/div/div[2]/span').text
        return down, up

    def tweet_at_provider(self, twitter_user_name, twitter_password, msg):
        """
        Tweets the complaint to Internet provider
        :param twitter_user_name: Twitter username
        :param twitter_password:  Twitter password
        :param msg: Tweet with download and upload speed
        :return: nothing
        """
        self.driver.get(URL_TWITTER)
        sleep(3)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div/main/div/div/div/div[1]/div/div[3]/a['
                                          '2]/div/span/span').click()
        username = self.driver.find_element_by_name('session[username_or_email]')
        username.send_keys(twitter_user_name)
        password = self.driver.find_element_by_name('session[password]')
        password.send_keys(twitter_password)
        password.send_keys(Keys.ENTER)
        sleep(5)
        tweet = self.driver.find_element_by_css_selector('.public-DraftStyleDefault-block')
        tweet.send_keys(msg)
        send_tweet = self.driver.find_element_by_xpath('//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div['
                                                       '1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div['
                                                       '4]/div/div/div[2]/div/div/span/span')
        send_tweet.click()
        sleep(10)
        print(msg)
        self.driver.quit()
