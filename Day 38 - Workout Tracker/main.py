"""
This program implements workout tracker using Nutritionix, Google Sheets and Sheety API
"""

import requests
from datetime import datetime

# Initialize global constants
APP_ID = ''  # TODO: Nutritionix APP ID
API_KEY = ''  # TODO: Nutritionix API KEY
NUTRITIONIX_ENDPOINT = 'https://trackapi.nutritionix.com'
SHEETY_ENDPOINT = ''  # TODO: Your Sheety API endpoint
USERNAME = ''  # TODO: Your Sheety username
PASSWORD = ''  # TODO: Your Sheety password


def main():
    exercise_endpoint = f'{NUTRITIONIX_ENDPOINT}/v2/natural/exercise'
    input_exercises = input('Which exercises did you do?: ')

    # Nutritionix Authentication
    headers = {
        'x-app-id': APP_ID,
        'x-app-key': API_KEY
    }

    # Nutritionix API Data
    exercise_config = {
        'query': input_exercises
    }

    response = requests.post(url=exercise_endpoint, json=exercise_config, headers=headers)
    result = response.json()

    if len(result['exercises']) > 0:
        date = datetime.now().date().strftime('%d/%m/%Y')
        time = datetime.now().time().strftime('%X')

        print('Writing to Google Sheets...')
        for i in range(len(result['exercises'])):
            # Sheety API Data
            sheety_config = {
                'workout': {
                    'date': date,
                    'time': time,
                    'exercise': result['exercises'][i]['name'].title(),
                    'duration': result['exercises'][i]['duration_min'],
                    'calories': result['exercises'][i]['nf_calories']
                }
            }

            requests.post(url=SHEETY_ENDPOINT, json=sheety_config, auth=(USERNAME, PASSWORD))
        print('Done')
    else:
        print('Invalid Entries')


if __name__ == '__main__':
    main()
