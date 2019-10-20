from sqlalchemy.testing import db

from crawler.video_crawler import VideoCrawler
from models.video import *


class VideosController:
    def __init__(self, items):
        self.items = items

    def get_details(self, videoId):
        data = VideoCrawler({'id': videoId}).get_video_details()
        return {'duration': data['items'][0]['contentDetails']['duration'],
                'view_count': data['items'][0]['statistics']['viewCount']}

    def save_data(self):
        for i in range(len(self.items)):
            new_video = Video(
                video_url='https://www.youtube.com/watch?v=' + self.items[i]['snippet']['resourceId']['videoId'],
                title=self.items[i]['snippet']['title'],
                thumbnail_url=self.items[i]['snippet']['thumbnails']['default']['url'],
                full_image_url=self.items[i]['snippet']['thumbnails']['standard']['url']
            )
            more_info = self.get_details(self.items[i]['snippet']['resourceId']['videoId'])
            new_video.duration = more_info['duration']
            new_video.views = more_info['view_count']
            new_video.downloaded_thumbnail_path = ''
            new_video.downloaded_image_path = ''
            db.session.add(new_video)
        db.session.commit()
