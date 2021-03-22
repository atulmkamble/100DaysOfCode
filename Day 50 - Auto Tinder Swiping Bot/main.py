"""
This program implements Auto Tinder Swiping Bot
"""

# Import required libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep

# Initialize Global Constants
URL = 'https://tinder.com'
CHROME_WEB_DRIVER = 'C:/Development/chromedriver.exe'
USER_NAME = '' # TODO: Insert your facebook user name here
PASSWORD = '' # TODO: Insert your facebook password here


def main():
    driver = webdriver.Chrome(executable_path=CHROME_WEB_DRIVER)

    # Open URL and maximize window
    driver.get(URL)
    driver.maximize_window()
    sleep(2)

    # Click on login button
    login_button = driver.find_element_by_css_selector('.button')
    login_button.click()
    sleep(2)

    # Facebook login button click
    fb_login = driver.find_element_by_xpath('//*[@id="t--149300558"]/div/div/div[1]/div/div[3]/span/div[2]/button')
    fb_login.click()
    sleep(2)

    base_window = driver.window_handles[0]
    fb_login_window = driver.window_handles[1]
    driver.switch_to.window(fb_login_window)
    print(driver.title)
    sleep(2)

    username = driver.find_element_by_id('email')
    username.send_keys(USER_NAME)
    password = driver.find_element_by_id('pass')
    password.send_keys(PASSWORD)
    password.send_keys(Keys.ENTER)
    sleep(5)

    driver.switch_to.window(base_window)
    print(driver.title)
    sleep(2)

    location = driver.find_element_by_xpath('//*[@id="t--149300558"]/div/div/div/div/div[3]/button[1]/span')
    location.click()
    notifications = driver.find_element_by_xpath('//*[@id="t--149300558"]/div/div/div/div/div[3]/button[2]/span')
    notifications.click()
    offers = driver.find_element_by_xpath('//*[@id="t-1890905246"]/div/div[2]/div/div/div[1]/button/span')
    offers.click()
    sleep(30)

    for n in range(100):
        # Add 1 second delay between likes
        sleep(1)
        try:
            # Like the picture on screen
            print('called')
            like_button = driver.find_element_by_xpath(
                '//*[@id="t-1890905246"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[4]/button')
            like_button.click()

        except ElementClickInterceptedException:
            try:
                # Skip past the match popup
                match_popup = driver.find_element_by_xpath('.itsAMatch a')
                match_popup.click()
            except NoSuchElementException:
                sleep(2)

    sleep(5)
    driver.quit()


if __name__ == '__main__':
    main()
