from flask import Flask, request, jsonify

from crawler.playlist_crawler import *
from crawler.channel_crawler import *

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/playlist')
def get_videos_info_from_playlist():
    videos = PlaylistCrawler({'playlistId': request.args.get('playlist_id')}).get_videos()
    return jsonify(videos)


@app.route('/channel')
def get_videos_info_from_channel():
    videos = ChannelCrawler({'channelId': request.args.get('channel_id')}).get_videos()
    return jsonify(videos)


if __name__ == '__main__':
    app.run(debug=True)
