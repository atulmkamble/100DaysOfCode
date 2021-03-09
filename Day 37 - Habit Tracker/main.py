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

    requests.post(url=PIXELA_ENDPOINT, json=user_params)


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

    requests.post(url=GRAPH_ENDPOINT, json=graph_config, headers=HEADERS)


def create_pixel(input_date):
    """
    Creates pixel for the input date with input quantity
    :param input_date: Creates pixel at this date
    :return: nothing
    """
    PIXEL_CREATION_ENDPOINT = f'{PIXELA_ENDPOINT}/{USER_NAME}/graphs/{GRAPH_ID}'
    input_quantity = str(int(input('How many minutes did you code?: ')))

    pixel_config = {
        'date': input_date.strftime('%Y%m%d'),
        'quantity': input_quantity,
    }

    requests.post(url=PIXEL_CREATION_ENDPOINT, json=pixel_config, headers=HEADERS)


def edit_pixel(input_date):
    """
    Edits pixel for the input date with input quantity
    :param input_date: Edits pixel at this date
    :return: nothing
    """
    PIXEL_EDIT_ENDPOINT = f'{PIXELA_ENDPOINT}/{USER_NAME}/graphs/{GRAPH_ID}/{input_date.strftime("%Y%m%d")}'
    input_quantity = str(int(input('How many minutes did you code?: ')))

    pixel_edit = {
        'quantity': input_quantity
    }

    requests.put(url=PIXEL_EDIT_ENDPOINT, json=pixel_edit, headers=HEADERS)


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
    create_user()
    create_graph()
    create_pixel(dt.now())
    # edit_pixel(dt.now()))
    # delete_pixel(dt.now())


if __name__ == '__main__':
    main()
