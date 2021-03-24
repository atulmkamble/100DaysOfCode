"""
This file implements the InstaFollower class
"""

# Import required libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.common.exceptions import ElementClickInterceptedException

CHROME_DRIVER_PATH = 'C:/Development/chromedriver.exe'
URL = 'https://www.instagram.com'


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

    def login(self, username, password, url=URL):
        """
        Login to instagram account
        :param username: Instagram username
        :param password: Instagram password
        :param url: Instagram URL
        :return: Nothing
        """
        self.driver.get(f'{url}/accounts/login/')
        self.driver.maximize_window()
        sleep(5)
        self.driver.find_element_by_name('username').send_keys(username)
        self.driver.find_element_by_name('password').send_keys(password)
        self.driver.find_element_by_name('password').send_keys(Keys.ENTER)
        sleep(5)
        self.driver.find_element_by_css_selector('.cmbtv button').click()
        sleep(5)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
        sleep(5)

    def find_followers(self, target_account, url=URL):
        """
        Find the followers of the target account
        :param target_account: Intended target account
        :param url: Instagram URL
        :return: Nothing
        """
        self.driver.get(f'{url}/{target_account}')
        sleep(5)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a').click()
        sleep(3)
        modal = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]')
        for i in range(10):
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', modal)
            sleep(2)

    def follow(self):
        """
        Follows the followers
        :return: nothing
        """
        all_buttons = self.driver.find_elements_by_css_selector('li button')
        for button in all_buttons:
            try:
                button.click()
                sleep(1)
            except ElementClickInterceptedException:
                self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div/div[3]/button[2]').click()
        sleep(5)
