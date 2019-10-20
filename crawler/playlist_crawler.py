from crawler import Crawler


class PlaylistCrawler:

    def __init__(self, params=None):
        if params is None:
            params = {}
        self.params = {'part': 'snippet', 'maxResults': 1}
        self.params.update(params)

    def get_videos(self):
        result = Crawler(self.params).get_videos_data_from_playlist()
        videos = result['items']
        return videos
