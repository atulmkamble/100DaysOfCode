"""
This program implements Habit tracker via Pixela
"""

import requests
from datetime import datetime as dt

# Initialize global constants
USER_NAME = ''  # TODO: Enter your preferred username
TOKEN = ''  # TODO: Enter any random text as token
GRAPH_ID = 'graph1'
PIXELA_ENDPOINT = 'https://pixe.la/v1/users'
HEADERS = {
    'X-USER-TOKEN': TOKEN
}


def create_user():
    """
    Creates pixela user account
    :return: nothing
    """
    user_params = {
        'token': TOKEN,
        'username': USER_NAME,
        'agreeTermsOfService': 'yes',
        'notMinor': 'yes'
    }

    response = requests.post(url=PIXELA_ENDPOINT, json=user_params)
    print(response.text)


def create_graph():
    """
    Creates graph for the user
    :return: nothing
    """
    GRAPH_ENDPOINT = f'{PIXELA_ENDPOINT}/{USER_NAME}/graphs'

    graph_config = {
        'id': GRAPH_ID,
        'name': 'Coding Graph',
        'unit': 'Minutes',
        'type': 'int',
        'color': 'momiji',
    }

    response = requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=HEADERS)
    print(response.text)


def create_pixel(input_date, input_quantity):
    """
    Creates pixel for the input date with input quantity
    :param input_date: Creates pixel at this date
    :param input_quantity: Creates pixel with this quantity
    :return: nothing
    """
    PIXEL_CREATION_ENDPOINT = f'{PIXELA_ENDPOINT}/{USER_NAME}/graphs/{GRAPH_ID}'

    date_today = dt.now()

    pixel_config = {
        'date': input_date.strftime('%Y%m%d'),
        'quantity': input_quantity,
    }

    response = requests.post(url=PIXEL_CREATION_ENDPOINT, json=pixel_config, headers=HEADERS)
    print(response.text)


def edit_pixel(input_date, input_quantity):
    """
    Edits pixel for the input date with input quantity
    :param input_date: Edits pixel at this date
    :param input_quantity: Edits pixel with this quantity
    :return: nothing
    """
    PIXEL_EDIT_ENDPOINT = f'{PIXELA_ENDPOINT}/{USER_NAME}/graphs/{GRAPH_ID}/{input_date.strftime("%Y%m%d")}'

    pixel_edit = {
        'quantity': input_quantity
    }

    response = requests.put(url=PIXEL_EDIT_ENDPOINT, json=pixel_edit, headers=HEADERS)
    print(response.text)


def delete_pixel(input_date):
    """
    Deletes pixel for the input date
    :param input_date: Deletes pixel at this date
    :return: nothing
    """
    PIXEL_DELETE_ENDPOINT = f'{PIXELA_ENDPOINT}/{USER_NAME}/graphs/{GRAPH_ID}/{input_date.strftime("%Y%m%d")}'

    response = requests.delete(url=PIXEL_DELETE_ENDPOINT, headers=HEADERS)
    print(response.text)


def main():
    # create_user()
    # create_graph()
    create_pixel(dt(year=2021, month=3, day=7), '90')
    # edit_pixel(dt(year=2021, month=3, day=8), '90')
    # delete_pixel(dt(year=2021, month=3, day=8))


if __name__ == '__main__':
    main()
