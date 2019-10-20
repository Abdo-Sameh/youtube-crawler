from crawler import Crawler


class PlaylistService(Crawler):

    def get_videos(self):
        result = Crawler().videos_data_from_playlist(self.params)
        videos = result['items']
        return videos