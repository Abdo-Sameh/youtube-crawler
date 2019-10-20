from flask import Flask, request, jsonify

from crawler.playlist_crawler import *
from crawler.channel_crawler import *

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/playlist')
def get_videos_info_from_playlist():
    videos = PlaylistCrawler({'playlistId': request.args.get('playlistId')}).get_videos()
    return jsonify(videos)


@app.route('/channel')
def get_videos_info_from_channel():
    playlists = ChannelCrawler({'channelId': request.args.get('channelId')}).get_playlists()
    videos = []
    for i in range(len(playlists)):
        videos += PlaylistCrawler({'playlistId': playlists[i]}).get_videos()
    return jsonify(videos)


if __name__ == '__main__':
    app.run(debug=True)
