from dotenv import load_dotenv, find_dotenv
from flask import request, jsonify, Flask
# import logging
from flask_sqlalchemy import SQLAlchemy

from crawler.channel_crawler import *
from crawler.playlist_crawler import *
from cron_schedule import *
load_dotenv(find_dotenv())
app = Flask(__name__)

app.config.from_object(os.getenv('APP_SETTINGS'))
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# logging.basicConfig(filename='demo.log', level=logging.DEBUG)


from controllers.videos_controller import VideosController


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/playlist')
def get_videos_info_from_playlist():
    videos = PlaylistCrawler({'playlistId': request.args.get('playlistId')}).get_videos()
    VideosController(videos).save_data()
    return jsonify(videos)


@app.route('/channel')
def get_videos_info_from_channel():
    playlists = ChannelCrawler({'channelId': request.args.get('channelId')}).get_playlists()
    videos = []
    for i in range(len(playlists)):
        videos += PlaylistCrawler({'playlistId': playlists[i]}).get_videos()
    VideosController(videos).save_data()
    return jsonify(videos)


if __name__ == '__main__':
    run_task()
    app.run(debug=True, use_reloader=False)
