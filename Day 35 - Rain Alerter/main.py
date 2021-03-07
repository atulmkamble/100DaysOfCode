"""
This program implements a Rain Alerter
"""

import requests
from twilio.rest import Client

# Initialize constants
OWM_ENDPOINT = 'https://api.openweathermap.org/data/2.5/onecall'
API_KEY = ''  # TODO: Update your API_KEY
ACCOUNT_SID = ''  # TODO: Update your ACCOUNT_SID
AUTH_TOKEN = ''  # TODO: Update your AUTH_TOKEN


def main():
    parameters = {
        'lat': 18.5196,
        'lon': 73.8553,
        'exclude': 'current,minutely,daily',
        'appid': API_KEY,
    }

    will_rain = False

    with requests.get(OWM_ENDPOINT, params=parameters) as connection:
        connection.raise_for_status()
        data = connection.json()
        hourly_data = data['hourly'][:12]
        for hour in hourly_data:
            weather_condition_code = hour['weather'][0]['id']
            if weather_condition_code < 700:
                will_rain = True
        if will_rain:
            client = Client(ACCOUNT_SID, AUTH_TOKEN)
            message = client.messages.create(
                body="It is going to rain today. Remember to bring an ☂️",
                from_='',  # TODO: Update Twilio number
                to=''  # TODO: Update your number
            )
            print(message.status)


if __name__ == '__main__':
    main()
