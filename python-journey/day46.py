#type: ignore
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

header = {
    "USER-AGENT":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36"
}
requests = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date}/" , headers=header)
data = requests.text

soup = BeautifulSoup(data , "html.parser")
songs = soup.select("li ul li h3")
songs_name = [song.get_text().strip() for song in songs]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri=("SPOTIFY_REDIRECT_URI"),
        client_id=("SPOTIFY_CLIENT_ID"),
        client_secret=("SPOTIFY_CLIENT_SECRET"),
        show_dialog=True,
        cache_path="token.txt",
        username=("SPOTIFY_USERNAME"),
    )
)
user_id = sp.current_user()["id"]
print(user_id)



