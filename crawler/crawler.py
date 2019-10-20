import os
import requests


class Crawler:

    urls = {
        'playlist_url': 'https://www.googleapis.com/youtube/v3/playlistItems',
        'video_url': 'https://www.googleapis.com/youtube/v3/videos',
        'playlists_from_channel_url': 'https://www.googleapis.com/youtube/v3/playlists'
    }

    def __init__(self, params=None):
        if params is None:
            params = {}
        self.params = {'key': os.getenv('API_KEY')}
        self.params.update(params)

    def get_videos_data_from_playlist(self):
        response = requests.get(url=self.urls['playlist_url'], params=self.params)
        return response.json()

    def get_playlists_from_channel(self):
        response = requests.get(url=self.urls['playlists_from_channel_url'], params=self.params)
        return response.json()

    def get_video_data(self):
        response = requests.get(url=self.urls['video_url'], params=self.params)
        return response.json()
