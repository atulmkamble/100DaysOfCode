"""
This program plays the cookie clicker game in an aoutmated way using the Selenium Webdriver Browser
"""

# Import required libraries
from selenium import webdriver
from time import time


def main():
    chrome_driver_path = 'C:/Development/chromedriver.exe'  # TODO: Download the driver and use your folder path
    driver = webdriver.Chrome(chrome_driver_path)
    driver.get('http://orteil.dashnet.org/experiments/cookie/')

    cookie = driver.find_element_by_css_selector('#cookie')

    # Get item upgrade ids
    items = driver.find_elements_by_css_selector('#store div')
    item_ids = [item.get_attribute('id') for item in items]

    # Time trackers
    five_minutes = time() + 60 * 5
    five_seconds = time() + 5

    while True:
        cookie.click()

        # For every 5 seconds
        if time() >= five_seconds:
            # Get all upgrades prices
            all_prices = driver.find_elements_by_css_selector('#store b')
            item_prices = []
            for price in all_prices:
                if price.text != '':
                    cost = int(price.text.split('-')[1].strip().replace(',', ''))
                    item_prices.append(cost)

            # Create dictionary of items and prices
            cookie_upgrades = {}
            for n in range(len(item_prices)):
                cookie_upgrades[item_prices[n]] = item_ids[n]

            # Get current cookie count
            cookie_count = int(driver.find_element_by_id('money').text.replace(',', ''))

            # Purchase the affordable upgrade
            affordable_upgrades = {}
            for cost, id in cookie_upgrades.items():
                if cookie_count > cost:
                    affordable_upgrades[cost] = id
            highest_affordable_upgrade = max(affordable_upgrades)
            to_purchase_id = affordable_upgrades[highest_affordable_upgrade]

            # Purchase the upgrade
            driver.find_element_by_id(to_purchase_id).click()

            # Add another 5 seconds until next check
            five_seconds = time() + 5

        # After 5 minutes, stop the bot and check cookies per second count
        if time() > five_minutes:
            cookie_per_second = driver.find_element_by_id('cps').text
            print(cookie_per_second)
            # Quit after 5 minutes
            break

    # Quit the browser after 5 minutes
    driver.quit()


if __name__ == '__main__':
    main()
