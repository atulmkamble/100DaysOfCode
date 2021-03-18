# Import required libraries
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Initialize Global Constants
SPOTIPY_CLIENT_ID = ''  # TODO: Use your spotify client ID
SPOTIPY_CLIENT_SECRET = ''  # TODO: User your spotify client secret
BILLBOARD_URL = 'https://www.billboard.com/charts/hot-100/'


def main():
    # Initialize the object
    sp = spotipy.Spotify(
        auth_manager=SpotifyOAuth(
            scope='playlist-modify-private',
            redirect_uri='http://example.com',
            client_id=SPOTIPY_CLIENT_ID,
            client_secret=SPOTIPY_CLIENT_SECRET,
            show_dialog=True,
            cache_path='token.txt'
        )
    )

    # Get the spotify user ID
    user_id = sp.current_user()['id']

    # Get the date for which you have to create the playlist
    date = input('Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ')
    print('Getting songs from Billboard')
    response = requests.get(f'{BILLBOARD_URL}{date}')
    soup = BeautifulSoup(response.text, 'html.parser')
    song_tags = soup.find_all(name='span', class_='chart-element__information__song text--truncate color--primary')

    # Saves the 100 song names from Billboard URL into a list
    songs_list = [song.getText() for song in song_tags]
    print('Completed')

    # List to save spotify URIs corresponding to Billboard 100 songs
    print('Searching songs in Spotify')
    song_uris = []
    year = date.split('-')[0]
    for song in songs_list:
        # Search the song in Spotify
        result = sp.search(q=f'track:{song} year:{year}', type='track')
        try:
            uri = result['tracks']['items'][0]['uri']
            song_uris.append(uri)
        except IndexError:
            print(f'"{song}" does not exist in Spotify. Skipped!')
    print('Completed')

    # Create a private playlist
    print('Adding songs to Spotify playlist')
    playlist = sp.user_playlist_create(user=user_id, name=f'{date} Billboard 100', public=False)

    # Add songs to that playlist
    sp.playlist_add_items(playlist_id=playlist['id'], items=song_uris)
    print('Completed')

    print(f"Newly Created Spotify Playlist URL: {playlist['external_urls']['spotify']}")


if __name__ == '__main__':
    main()
