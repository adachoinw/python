import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

time = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

URL = f"https://www.billboard.com/charts/hot-100/{time}/"
CLIENT_ID = "9154920e2b6041388c46d9ea1cd2aa97"
CLIENT_SECRET = "3dc77e8c3f5d4f90961c9ef7af29a034"
REDIRECT_URI = "http://localhost:8888/callback"

response = requests.get(URL)
billboard_page = response.text

soup = BeautifulSoup(billboard_page, "html.parser")

song_titles = soup.find_all(name="h3", class_="u-max-width-230@tablet-only")

title_list = [title.getText().strip() for title in song_titles]
pprint(title_list)

#### SPOTIFY AUTHENTICATION ####


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               show_dialog=True,
                                               scope="playlist-modify-private",
                                               cache_path="token.txt"))

user_id = sp.current_user()["id"]


song_uris = []
year = time.split("-")[0]

for song in title_list:
    result = sp.search(q=f"track: {song} year: {year}", type="track")
    # pprint(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
        # print(f"{song}: {uri}")
    except IndexError:
        print(f"{song} doesn't exist in spotify")

new_playlist = sp.user_playlist_create(user=user_id, name=f"{time} Billboard 100", public=False)
# print(new_playlist)
sp.playlist_add_items(playlist_id=new_playlist, items=song_uris, position=None)
