from crawler.video_crawler import *
from models.video import *


class VideosController:
    def __init__(self, items):
        self.items = items

    def get_details(self, videoId):
        data = VideoCrawler({'id': videoId}).get_video_details()
        return {'duration': data[0]['contentDetails']['duration'],
                'view_count': data[0]['statistics']['viewCount']}

    def download_image(self, url, video_id):
        download_path = 'images/' + video_id
        if not os.path.exists(download_path):
            os.makedirs(download_path)
        response = requests.get(url)
        with open(download_path + '/' + url.split('/')[-1], 'wb') as f:
            f.write(response.content)
        return os.getcwd() + '/' + download_path

    def save_data(self):
        for i in range(len(self.items)):
            more_info = self.get_details(self.items[i]['snippet']['resourceId']['videoId'])
            video_id = self.items[i]['snippet']['resourceId']['videoId']
            new_video = Video(
                video_url='https://www.youtube.com/watch?v=' + video_id,
                title=self.items[i]['snippet']['title'],
                thumbnail_url=self.items[i]['snippet']['thumbnails']['default']['url'],
                full_image_url=self.items[i]['snippet']['thumbnails']['standard']['url']
            )
            thumbnail_path = self.download_image(self.items[i]['snippet']['thumbnails']['default']['url'], video_id)
            full_image_path = self.download_image(self.items[i]['snippet']['thumbnails']['standard']['url'], video_id)
            new_video.duration = more_info['duration']
            new_video.views = more_info['view_count']
            new_video.downloaded_thumbnail_path = thumbnail_path
            new_video.downloaded_image_path = full_image_path
            db.session.add(new_video)
        db.session.commit()
