"""
This program implements a Birthday Wisher. It randomly selects a birthday card and sends it over email.
"""

# Import required libraries
import datetime as dt
import pandas as pd
from random import randint
import smtplib
from art import logo


def main():
    # Greet the user
    print(logo)

    # Declare Constants
    MY_EMAIL = ''  # TODO: Replace this with your email
    MY_PASSWORD = ''  # TODO: Replace this with your password
    TO_REPLACE = '[NAME]'

    # Get today's date components
    today = dt.datetime.now()
    year = today.year
    month = today.month
    day = today.day
    birthday_names = []
    is_birthday = False

    try:
        # Read the birthdays file
        df = pd.read_csv('birthdays.csv')  # TODO: Update this file with birthdays of your loved once
    except FileNotFoundError:
        print('There is no file to read. Make sure you have the birthdays.csv file in this folder')
    else:
        birthday_dict = df.to_dict(orient='records')
        # Check if today is someone's birthday
        for birthday in birthday_dict:
            if int(birthday['month']) == month:
                if int(birthday['day']) == day:
                    # If yes, save the name
                    is_birthday = True
                    birthday_names.append(birthday['name'].title())

    if is_birthday:
        print('Today is a birthday for:')
        for name in birthday_names:
            print(name)
        # Choose a random letter
        with open(f'./letter_templates/letter_{randint(1, 3)}.txt') as f:
            contents = f.read()
            print('\nSending emails ...')
            for name in birthday_names:
                contents_modified = contents.replace(TO_REPLACE, name)
                # Send it via email
                with smtplib.SMTP('smtp.gmail.com') as connection:  # TODO: If your email is other than gmail replace
                    # the SMTP server here
                    connection.starttls()
                    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                    connection.sendmail(
                        from_addr=MY_EMAIL,
                        to_addrs=MY_EMAIL,  # TODO: Change the recipient's email here
                        msg=f'Subject:Happy Birthday\n\n{contents_modified}'
                    )
            print('Emails sent successfully')
    else:
        print('No Birthdays Today')


if __name__ == '__main__':
    main()
