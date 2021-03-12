from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

ORIGIN_CITY_IATA = 'LON'


def main():
    data_manager = DataManager()
    sheet_data = data_manager.read_data()
    flight_search = FlightSearch()
    notification_manager = NotificationManager()

    if len(sheet_data) > 0:
        for row in sheet_data:
            if row['iataCode'] == '':
                row['iataCode'] = flight_search.search_iata(row['city'])
            data_manager.destination_data = sheet_data
            data_manager.update_data()
        sheet_data = data_manager.read_data()

    destinations = {
        data["iataCode"]: {
            "id": data["id"],
            "city": data["city"],
            "price": data["lowestPrice"]
        } for data in sheet_data}

    tomorrow = datetime.now() + timedelta(days=1)
    six_months_from_today = datetime.now() + timedelta(days=180)

    for destination in destinations:
        flight = flight_search.search_flights(
            ORIGIN_CITY_IATA,
            destination['iataCode'],
            from_time=tomorrow,
            to_time=six_months_from_today
        )

        if flight is None:
            continue

        if flight.price < sheet_data[destination]['price']:
            users = data_manager.get_customer_emails()
            emails = [row['email'] for row in users]
            names = [row['firstName'] for row in users]

            msg = f'Low price alert! Only £{flight.price} to fly from {flight.origin_city}-{flight.origin_airport} '
            f'to {flight.destination_city}-{flight.destination_airport}, from {flight.out_date} '
            f'to {flight.return_date}.'

            if flight['stop_overs'] > 0:
                msg += f'\nFlight has {flight["stop_overs"]} stop over, via {flight["via_city"]}'

            link = f'https://www.google.co.uk/flights?hl=en#flt={flight.origin_airport}.{flight.destination_airport}' \
                   f'.{flight.out_date}*{flight.destination_airport}.{flight.origin_airport}.{flight.return_date}'

            notification_manager.send_emails(emails, msg, link)


if __name__ == '__main__':
    main()
