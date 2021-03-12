import requests

# TODO: Add your Sheety account details
SHEETY_ENDPOINT = ''
USERNAME = ''
PASSWORD = ''


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def read_data(self):
        response = requests.get(url=SHEETY_ENDPOINT)
        self.destination_data = response.json()['prices']
        return self.destination_data

    def update_data(self):
        for i in self.destination_data:
            sheety_edit_endpoint = f'{SHEETY_ENDPOINT}/{i["id"]}'
            record_edit = {
                'price': {
                    'iataCode': i['iataCode']
                }
            }
            requests.put(url=sheety_edit_endpoint, json=record_edit, auth=(USERNAME, PASSWORD))

    def get_customer_emails(self):
        customers_endpoint = '' # TODO: Add the sheety users sheet API endpoint
        response = requests.get(url=customers_endpoint)
        data = response.json()
        customer_data = data['users']
        return customer_data
