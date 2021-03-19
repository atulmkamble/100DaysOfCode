"""
A program to track Amazon product price as per your desired threshold price for deals
"""

# Import required libraries
import requests
from bs4 import BeautifulSoup
import smtplib

# Initialize Global constants
MY_EMAIL = ''  # TODO: Replace with your email
MY_PASSWORD = ''  # TODO: Replace with your password
# The product that you want to track (in this case it a Playstation 4)
URL = 'https://www.amazon.com/PlayStation-4-Console-1TB-Slim/dp/B074LRF639/'


def main():
    headers = {
        'Accept-Language': 'en-US,en;q=0.9',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36'
    }

    # Make request and get the response
    response = requests.get(URL, headers=headers)
    soup = BeautifulSoup(response.content, 'lxml')

    # Get the price and title of the product
    price_tag = soup.find(id='priceblock_ourprice')
    current_price = float(price_tag.getText().split('$')[1])
    title = soup.find(id='productTitle').getText().strip()

    # If the price is less than or equal to your desired price, then send an email
    if current_price <= 350:
        with smtplib.SMTP('smtp.gmail.com') as connection:  # TODO: Replace with your email's SMTP server
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f'Subject:Amazon Price Alert\n\n{title} is now {current_price}.')


if __name__ == '__main__':
    main()
