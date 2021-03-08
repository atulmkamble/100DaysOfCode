import requests
from twilio.rest import Client

# Initialize global constants
# STOCK_NAME = "TSLA"
# COMPANY_NAME = "Tesla Inc"
STOCK_NAME = "MSFT"
COMPANY_NAME = "Microsoft"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = ''  # TODO: Update the Stock API Key
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = ''  # TODO: Update the News API Key
ACCOUNT_SID = ''  # TODO: Update Twilio SID
AUTH_TOKEN = ''  # TODO: Update Twilio Auth Token
STOCK_DIRECTION = ''


def get_news(pct_diff):
    """
    This function gets the news from an API related to the stock
    :param pct_diff: Percent difference of the stocks on the prior day
    :return: nothing
    """
    global STOCK_DIRECTION
    parameters_news = {
        'qInTitle': COMPANY_NAME,
        'sortBy': 'publishedAt',
        'apiKey': NEWS_API_KEY,
    }

    # Access News API
    with requests.get(NEWS_ENDPOINT, params=parameters_news) as news_connection:
        news_connection.raise_for_status()
        news_data = news_connection.json()
        news_data = news_data['articles'][:3]

    # Get the top three articles in (Headline, Brief) format
    articles = [(article['title'], article['description']) for article in news_data]

    # Set the direction indicator
    if pct_diff > 5:
        STOCK_DIRECTION = '🔺'
    elif pct_diff < -5:
        STOCK_DIRECTION = '🔻'

    # Format the message and send via Twilio
    for article in articles:
        msg = f'''
        {STOCK_NAME}: {STOCK_DIRECTION}{abs(pct_diff)}%
        Headline: {article[0]}
        Brief: {article[1]}
        '''
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        message = client.messages.create(
            body=msg,
            from_='',  # TODO: Update Tiwilo number
            to=''  # TODO: Update receiver's number
        )


def main():
    # Connect to Stock Endpoint and get the closing prices for last 2 business days
    parameters_stock = {
        'function': 'TIME_SERIES_DAILY',
        'symbol': STOCK_NAME,
        'apikey': STOCK_API_KEY
    }

    with requests.get(STOCK_ENDPOINT, params=parameters_stock) as connection:
        connection.raise_for_status()
        data = connection.json()
        data = data['Time Series (Daily)']
        closing_value_list = [float(val['4. close']) for (key, val) in data.items()][:2]
        diff = round(closing_value_list[1] - closing_value_list[0], 2)
        pct_diff = round(diff / closing_value_list[0] * 100, 2)
        if pct_diff > 5 or pct_diff < -5:
            # Get news corresponding to the stock
            get_news(pct_diff)


if __name__ == '__main__':
    main()
