"""
This program implements Internet Speed Twitter Complaint Bot
"""

# Import required class
from internet_speed import InternetSpeedTwitterBot

# Initialize Global Constants
PROMISED_DOWN = 60
PROMISED_UP = 60
TWITTER_USER_NAME = ''  # TODO: Fill in your Twitter username
TWITTER_PASSWORD = ''  # TODO: Fill in your Twitter password


def main():
    twitter_bot = InternetSpeedTwitterBot()
    down, up = twitter_bot.get_internet_speed()
    print(f'Down: {down}, Up: {up}')
    if float(down) < PROMISED_DOWN or float(up) < PROMISED_UP:
        msg = f'Hey Internet Provider, why is my internet speed {down}down/{up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up '
        twitter_bot.tweet_at_provider(TWITTER_USER_NAME, TWITTER_PASSWORD, msg)
    print('Done')


if __name__ == '__main__':
    main()
