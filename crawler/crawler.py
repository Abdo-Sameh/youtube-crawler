import os
import requests


class Crawler:

    urls = {
        'playlist_url': 'https://www.googleapis.com/youtube/v3/playlistItems',
        'channel_search': 'https://www.googleapis.com/youtube/v3/search',
        # 'video_url': 'https://www.googleapis.com/youtube/v3/videos',
        # 'playlist_by_channel_url': 'https://www.googleapis.com/youtube/v3/playlists'
    }

    def __init__(self, params=None):
        if params is None:
            params = {}
        self.params = {'part': 'snippet', 'maxResults': 2, 'key': os.getenv('API_KEY')}
        self.params.update(params)

    def videos_data_from_playlist(self, params):
        response = requests.get(url=self.urls['playlist_url'], params=self.params)
        return response.json()

    def videos_data_from_channel(self, params):
        response = requests.get(url=self.urls['channel_search'], params=self.params)
        return response.json()
