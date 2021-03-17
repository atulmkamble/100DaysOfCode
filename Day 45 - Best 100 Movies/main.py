"""
This program scraps the data from a website to get 100 best movies of all time and writes it to a file
"""

import requests
from bs4 import BeautifulSoup

# Initialize global constants
URL = 'https://www.hollywoodreporter.com/lists/100-best-films-ever-hollywood-favorites-818512'


def main():
    # Scrape the data from URL
    with requests.get(URL) as movies_file:
        data = movies_file.text

    # Get the movie titles
    soup = BeautifulSoup(data, 'html.parser')
    movie_titles = soup.find_all(name='h1', class_='list-item__title')

    movies_list = []
    # Prepare the data as per the format
    i = 100
    for movie in movie_titles:
        movies_list.append(f'{i}) {movie.getText()}\n')
        i -= 1

    # Reverse the list since 100th movie is at the first place
    movies_list = movies_list[::-1]

    # Write the data to a file
    with open('movies.txt', 'w') as m_file:
        for movie in movies_list:
            m_file.write(movie)


if __name__ == '__main__':
    main()
