from crawler import *


class ChannelCrawler:

    def __init__(self, params=None):
        if params is None:
            params = {}
        self.params = {'part': 'snippet', 'maxResults': 1}
        self.params.update(params)

    def get_playlists(self):
        result = Crawler(self.params).get_playlists_from_channel()
        playlists = []
        print result
        for i in range(len(result['items'])):
            playlists += [result['items'][i]['id']]
        return playlists
