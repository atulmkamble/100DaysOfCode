import requests
from flight_data import FlightData

FLIGHT_API_ENDPOINT = "https://tequila-api.kiwi.com"
API_KEY = '' # TODO: Add your API key


class FlightSearch:
    def search_iata(self, city):
        headers = {
            'apikey': API_KEY
        }
        parameters = {
            'term': city,
            'location_types': 'city'
        }
        response = requests.get(url=f'{FLIGHT_API_ENDPOINT}/locations/query', params=parameters, headers=headers)
        return response.json()['locations'][0]['code']

    def search_flights(self, origin_city_code, destination_city_code, from_time, to_time):
        headers = {
            'apikey': API_KEY
        }
        parameters = {
            'fly_from': origin_city_code,
            'fly_to': destination_city_code,
            'date_from': from_time.strftime('%d/%m/%Y'),
            'date_to': to_time.strftime('%d/%m/%Y'),
            'nights_in_dst_from': 7,
            'nights_in_dst_to': 28,
            'one_for_city': 1,
            'max_stopovers': 0,
            'curr': 'GBP'
        }
        response = requests.get(url=f'{FLIGHT_API_ENDPOINT}v2/search', params=parameters, headers=headers)

        try:
            data = response.json()['data'][0]
        except IndexError:
            parameters['max_stopovers'] = 1
            response = requests.get(
                url=f"{FLIGHT_API_ENDPOINT}/v2/search",
                headers=headers,
                params=parameters
            )
            data = response.json()['data'][0]
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][1]["cityTo"],
                destination_airport=data["route"][1]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][2]["local_departure"].split("T")[0],
                stop_overs=1,
                via_city=data["route"][0]["cityTo"]
            )
            return flight_data
        else:
            flight_data = FlightData(
                price=data["price"],
                origin_city=data["route"][0]["cityFrom"],
                origin_airport=data["route"][0]["flyFrom"],
                destination_city=data["route"][0]["cityTo"],
                destination_airport=data["route"][0]["flyTo"],
                out_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )
            return flight_data
