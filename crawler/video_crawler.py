from crawler import Crawler


class VideoCrawler:

    def __init__(self, params=None):
        if params is None:
            params = {}
        self.params = {'part': 'statistics,contentDetails'}
        self.params.update(params)

    def get_video_details(self):
        result = Crawler(self.params).get_video_data()
        return result
