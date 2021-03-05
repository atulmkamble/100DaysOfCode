"""
This program notifies you if the International Space Station is above your location at night time.
"""

import requests
from datetime import datetime
from time import sleep
import smtplib

MY_LAT = 18.520430  # TODO: Replace with your latitude
MY_LONG = 73.856743  # TODO: Replace with your longitude
MY_EMAIL = ''  # TODO: Replace with your email
MY_PASSWORD = ''  # TODO: Replace with your password


def pos_within_error(lat, long, iss_lat, iss_long):
    """
    Return if the current position is withing the error limits of ISS position
    :param lat: Your latitude
    :param long: Your longitude
    :param iss_lat: ISS latitude
    :param iss_long: ISS longitude
    :return:
    """
    if (lat - 5 <= iss_lat <= lat + 5) and (long - 5 <= iss_long <= long + 5):
        return True
    else:
        return False


def main():
    while True:
        # Check every 60 seconds
        sleep(60)

        # Get the ISS position
        response = requests.get(url="http://api.open-notify.org/iss-now.json")
        response.raise_for_status()
        data = response.json()

        iss_latitude = float(data["iss_position"]["latitude"])
        iss_longitude = float(data["iss_position"]["longitude"])

        # Check if your position is within +5 or -5 degrees of the ISS position
        is_within_range = pos_within_error(MY_LAT, MY_LONG, iss_latitude, iss_longitude)

        if is_within_range:
            # Check the sunrise and sunset times at your location
            parameters = {
                "lat": MY_LAT,
                "lng": MY_LONG,
                "formatted": 0,
            }

            response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
            response.raise_for_status()
            data = response.json()
            sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
            sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

            # Check the current time
            time_now = datetime.now()
            current_hour = time_now.hour

            # If ISS is above your and it is night time, trigger an email to look up for ISS
            if current_hour >= sunset or current_hour <= sunrise:
                with smtplib.SMTP('smtp.gmail.com') as connection:  # TODO: Replace with your email's SMTP server
                    connection.starttls()
                    connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                    connection.sendmail(
                        from_addr=MY_EMAIL,
                        to_addrs=MY_EMAIL,
                        msg='Subject:Look Up for ISS\n\nThe ISS is currently above you. Look up to spot it in the sky.')
            else:
                print('The ISS is overhead but you cannot spot it in daytime')


if __name__ == '__main__':
    main()
