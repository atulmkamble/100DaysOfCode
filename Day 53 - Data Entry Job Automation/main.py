"""
This program fetches the rent details from Zillow and writes it to a Google form
"""

# Import required libraries
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from time import sleep

# Initialize Global Variables
ZILLOW_URL = '' # TODO: The Zillow URL that you want to scrape
CHROME_DRIVER_PATH = 'C:/Development/chromedriver.exe' # TODO: Path to chrome driver
GOOGLE_FORM_URL = '' # TODO: Your google form link
HEADER = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/89.0.4389.90 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9'
} # TODO: Your Browser header details (can be obtained at http://myhttpheader.com/)


def main():
    # Goto Zillow URL and fetch data
    response = requests.get(ZILLOW_URL, headers=HEADER)
    data = response.text
    soup = BeautifulSoup(data, 'html.parser')

    # Get the links, addresses, rent amounts and descriptions
    all_link_elements = soup.select('.list-card-top a')
    all_links = []
    for link in all_link_elements:
        # print(link.prettify())
        href = link['href']
        if 'http' not in href:
            all_links.append(f'https://www.zillow.com{href}')

    all_address_elements = soup.select('.list-card-info address')
    all_addresses = []
    for address in all_address_elements:
        all_addresses.append(address.getText())

    all_rent_elements = soup.select('.list-card-price')
    all_rents = []
    for rent in all_rent_elements:
        all_rents.append((((rent.getText().split('+')[0]).split('/')[0]).split()[0]))

    all_description_elements = soup.select('.list-card-details')
    all_desc = []
    for desc in all_description_elements:
        all_desc.append(desc.getText())

    # Initialize Selenium driver
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)

    # Fill in the Google Form
    for i in range(len(all_links) - 1):
        driver.get(GOOGLE_FORM_URL)
        sleep(2)
        desc = driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
        desc.send_keys(all_desc[i])

        address = driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        address.send_keys(all_addresses[i])

        rent_amount = driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        rent_amount.send_keys(all_rents[i])

        link = driver.find_element_by_xpath(
            '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input')
        link.send_keys(all_links[i])

        submit = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div')
        submit.click()

    print('Done')


if __name__ == '__main__':
    main()
