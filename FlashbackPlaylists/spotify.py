import time

from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from spotipy.exceptions import SpotifyException


class PlaylistGenerator:

    def generate_playlist(date, title, description):

        CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
        SECRET = os.environ.get("SPOTIFY_SECRET")
        REDIRECT_URL = "http://example.com"
        OAUTH_AUTHORIZE_URL = 'https://accounts.spotify.com/authorize'
        OAUTH_TOKEN_URL = 'https://accounts.spotify.com/api/token'

        # connect to Spotify Account
        sp = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                scope="playlist-modify-public",
                redirect_uri=REDIRECT_URL,
                client_id=CLIENT_ID,
                client_secret=SECRET,
                show_dialog=True,
                cache_path="FlashbackPlaylists/.cache",
                username="timonrieger",
            )
        )

        user_id = sp.current_user()["id"]

        # response = requests.get(
        #     url="https://www.billboard.com/charts/hot-100/" + date + "/")
        # website_html = response.text
        #
        # soup = BeautifulSoup(website_html, "html.parser")
        #
        # song_name = soup.select(selector="ul li ul li h3")
        # song_list = [song.getText().strip() for song in song_name]
        #
        # year = date.split("-")[0]
        #
        # # get the uri for each song and append it to the list song_uris
        # song_uris = []
        # for song in song_list:
        #     try:
        #         uri = sp.search(q=f"track:{song} year:{year}")[
        #             "tracks"]["items"][0]["uri"]
        #         song_uris.append(uri)
        #     except IndexError:
        #         pass
        #
        #
        # # create private playlist
        # print(song_uris)
        # time.sleep(30)
        song_uris = ['spotify:track:34WBFKc2eVRkQO7N1lKRsB', 'spotify:track:2StLwKcI9wreel3XEzljbl', 'spotify:track:522NAdIqTRVdmPEuTODmdR', 'spotify:track:1Ezz8SBpkRWjtBFvosdCNq', 'spotify:track:5CXHxFMW05L75D7B7SwHwk', 'spotify:track:2PUykQgPRSELZ0ZHl47Oz0', 'spotify:track:5Bpl1UjmKKYkqC3uxlSOWj', 'spotify:track:68DSRY0cKfA0P6nVlxoSmX', 'spotify:track:3FkQN4NyCFlfn7fWzBkWCj', 'spotify:track:4tcxjwBBjEMIqqosRDqKFO', 'spotify:track:3xXTY1IBKt14VTl2LMqCzi', 'spotify:track:0CX4g0kHJoMV8TKHU8PoOT', 'spotify:track:7dY6H9cMUGTEcK5iWoOs5T', 'spotify:track:7vP3yOZowjN017VZYGH3hy', 'spotify:track:1RsxUuB1Q5OdseLpHMBkEN', 'spotify:track:5KDT5BDSmomPMe2AXuGInR', 'spotify:track:5J8OTXuf2y2nFmNjilRkTu', 'spotify:track:2BcYKt7t4kfllFJGiaBGsQ', 'spotify:track:4QITKZ6SIV1eL5vJdeicRo', 'spotify:track:3c6vdiLeV9DUbTMWk5H3se', 'spotify:track:4WAo3JauonCmRiyMU4qXQn', 'spotify:track:2wzOmiSpq2WlsN6x4XkLcs', 'spotify:track:5GFhzF0nLXRsZS9PeLry7p', 'spotify:track:6CjId5Ur6jRP6ndGLy6vm2', 'spotify:track:5yNUgA66PbcPIJPOU2eBwR', 'spotify:track:1L34bevNmqk5mXYdoCAcyP', 'spotify:track:605RcpKH2IaZHnbF163SeL', 'spotify:track:0upLyFR8Rr52ZpMp5esQoq', 'spotify:track:45NSm9MKUGJ8NlWkNuKJzo', 'spotify:track:1ruOHeS4yg9Q939Qgk4Gbr', 'spotify:track:3CDObpDCqsPlt40sJh3fuj', 'spotify:track:7nVQ8mo77KaUvhUQzh4vMy', 'spotify:track:3qxBN4nWvSDibXmEq5of9E', 'spotify:track:05PjI4vVQq7Nqj1iyE5Vc9', 'spotify:track:0Eq4BMgsdV6DkLSJfX8eBt', 'spotify:track:1E4RsQK6cqhVimzsopfO0E', 'spotify:track:4MTneGoerBQyRqjTrlD02t', 'spotify:track:4OZWBhQOycXtldDdJOMXUr', 'spotify:track:6CP8uQV58S9gHtq68etkzR', 'spotify:track:1HvZgqzkwgrucRYehilPee', 'spotify:track:1sXVnVkPsLm64t9rZmCQsi', 'spotify:track:1JL223WRtrU0BI9a3Qw1Ks', 'spotify:track:5VbePtZp1at8gH990zVyTI', 'spotify:track:474iAHLvDbXAQnEI82i4RW', 'spotify:track:0iI2fbR06lKJE6wSYmYQch', 'spotify:track:3XpzjXC9aSKBDL68gMpvSO', 'spotify:track:41Gu4TUd7jdj9MWGG9uYnI', 'spotify:track:507kW5xEVxuJ0oPa3pM8Ct', 'spotify:track:1vRANBoQ9xVT8nEMOO0S58', 'spotify:track:3e7bMUM2jFwEYBgDqWCBDs', 'spotify:track:5AZWCkUOnu2KM6Q5iEoGpI', 'spotify:track:5VgHd81t0v4XZBfhkd1UU6', 'spotify:track:6T5ijGkSINcoCGEejEF7fO', 'spotify:track:0bS47FtHCwevy3xGforak0', 'spotify:track:1dRYWSK5mpIN3JGE7vMtSx', 'spotify:track:1UiKUFbCfgbVjwY8W657Pv', 'spotify:track:7exMLNXpgDikI76FLqQL3V', 'spotify:track:6R5gOBB9UInTZ0Hp0bX1kp', 'spotify:track:1UiKUFbCfgbVjwY8W657Pv', 'spotify:track:5JADndYiIq9QTpIr0KhnfU']

        max_retries = 3
        retries = 0
        wait_time = 10  # Initial wait time in seconds

        while retries < max_retries:
            try:
                print(user_id)
                create_playlist = sp.user_playlist_create(user=user_id, name=title, public=True,
                                                          description=description)
                # If the playlist creation is successful, exit the loop
                # use the playlist id to add the song (uri) to the playlist
                sp.playlist_add_items(playlist_id=create_playlist["id"], items=song_uris)

                # get playlist url
                playlist_url = create_playlist["external_urls"]["spotify"]

                return playlist_url
            except SpotifyException as e:
                if e.http_status == 429:
                    # If the error is due to rate limiting (429), retry with exponential backoff
                    print(f"Rate limited. Waiting for {wait_time} seconds before retrying...")
                    time.sleep(wait_time)
                    wait_time *= 2  # Exponential backoff
                    retries += 1
                else:
                    # If the error is not rate limiting related, raise the exception again
                    raise e

        if retries == max_retries:
            # If max retries reached without success, raise an exception or handle the error accordingly
            raise Exception("Max retries reached. Unable to create playlist.")


