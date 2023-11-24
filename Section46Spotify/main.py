import requests
import html
from bs4 import BeautifulSoup
from decouple import config
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

spotify_clientId = config("spotify_clientId")
spotify_clientSecret = config("spotify_clientSecret")
BILLBOARD_BASE_URL = "https://www.billboard.com/charts/hot-100/"

date = input("What year do you want to travel to? Type the date in this format: YYYY-MM-DD:\n")

billboard_response = requests.get(f"{BILLBOARD_BASE_URL}/{date}")
billboard_soup = BeautifulSoup(billboard_response.text, 'html.parser')

songs = [song.getText().replace("\n", "").replace("\t", "") for song in billboard_soup.select(selector="li ul li #title-of-a-story")]
artists = [artist.getText().replace("\n", "").replace("\t", "") for artist in billboard_soup.select(selector="li ul .o-chart-results-list__item .a-font-primary-s")]

artist_and_song = []
for index in range(0, 25):
    obj = {
        "artist": artists[index],
        "song": songs[index]
    }
    artist_and_song.append(obj)
    
    
sp = spotipy.Spotify(auth_manager=spotipy.SpotifyOAuth(client_id=spotify_clientId, client_secret=spotify_clientSecret, redirect_uri="http://example.com", scope="playlist-modify-private"))
user = sp.current_user()

song_uris = []
for song in artist_and_song:
    html_song = html.escape(song['song'])
    html_artist = html.escape(song['artist'])
    result = sp.search(f"track:{html_song} artist:{html_artist.split("Featuring")[0]}", limit=1, type="track")
    try:
        song_uris.append(result['tracks']['items'][0]['uri'])
    except IndexError:
        print(f'could not find song {song['song']} by {song['artist']}')
    
new_playlist = sp.user_playlist_create(user=user['id'], name=f"{date} Billboard Top Songs", public=False)
print(new_playlist['id'])

sp.playlist_add_items(playlist_id=new_playlist['id'], items=song_uris)



