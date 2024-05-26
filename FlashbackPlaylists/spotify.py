from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os

class PlaylistGenerator:

    def __init__(self):
        self.CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
        self.SECRET = os.environ.get("SPOTIFY_SECRET")

    def generate_playlist(self, date, title, description):
        # Scraping Billboard 100
        response = requests.get("https://www.billboard.com/charts/hot-100/" + date)
        soup = BeautifulSoup(response.text, 'html.parser')
        song_names_spans = soup.select("li ul li h3")
        song_names = [song.getText().strip() for song in song_names_spans]

        # Spotify Authentication
        sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                scope="playlist-modify-public",
                redirect_uri="http://example.com",
                client_id=self.CLIENT_ID,
                client_secret=self.SECRET,
                show_dialog=True,
                cache_path="FlashbackPlaylists/token.txt"
            )
        )
        user_id = sp.current_user()["id"]

        # Searching Spotify for songs by title
        song_uris = []
        year = date.split("-")[0]
        for song in song_names:
            result = sp.search(q=f"track:{song} year:{year}", type="track")
            try:
                uri = result["tracks"]["items"][0]["uri"]
                song_uris.append(uri)
            except IndexError:
                continue

        # Creating a new private playlist in Spotify
        playlist = sp.user_playlist_create(user=user_id, name=title, public=True, description=description)

        # Adding songs found into the new playlist
        sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
        return playlist["external_urls"]["spotify"]


