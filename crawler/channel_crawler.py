from crawler import *


class ChannelCrawler(Crawler):

    def get_videos(self):
        result = Crawler().videos_data_from_channel(self.params)
        videos = result['items']
        return videos
