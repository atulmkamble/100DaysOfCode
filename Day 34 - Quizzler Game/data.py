"""
This file gets the data from Open Trivia API
"""

import requests

parameters = {
    'amount': 10,
    'category': 18,
    'type': 'boolean',
}

with requests.get('https://opentdb.com/api.php', params=parameters) as connection:
    connection.raise_for_status()
    data = connection.json()
    question_data = data['results']
