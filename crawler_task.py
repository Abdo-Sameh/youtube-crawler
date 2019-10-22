from crawler.video_crawler import VideoCrawler
from models.video import *


def update_record(old_record, new_data):

    old_record.title = new_data[0]['snippet']['title']
    old_record.image = new_data[0]['snippet']['thumbnails']['default']['url']
    old_record.thumbnail = new_data[0]['snippet']['thumbnails']['standard']['url']
    old_record.duration = new_data[0]['contentDetails']['duration']
    old_record.views = new_data[0]['statistics']['viewCount']
    return old_record


def download_image(url, video_id):
    download_path = 'images/' + video_id
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    response = requests.get(url)
    with open(download_path + '/' + url.split('/')[-1], 'wb') as f:
        f.write(response.content)
    return os.getcwd() + '/' + download_path


def update_data():
    videos = Video.query.all()
    for i in range(len(videos)):
        print videos[i]
        url = videos[i].video_url
        video_id = url[url.find('v=') + 2:]
        new_data = VideoCrawler({'id': video_id, 'part': 'snippet,statistics,contentDetails'}).get_video_details()
        videos[i] = update_record(videos[i], new_data)
        thumbnail_path = download_image(new_data[0]['snippet']['thumbnails']['default']['url'], video_id)
        full_image_path = download_image(new_data[0]['snippet']['thumbnails']['standard']['url'], video_id)
        videos[i].downloaded_thumbnail_path = thumbnail_path
        videos[i].downloaded_image_path = full_image_path

    db.session().commit()


if __name__ == "__main__":
    update_data()
