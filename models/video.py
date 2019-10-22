from app import *


class Video(db.Model):
    """ Model for Video """
    __tablename__ = 'videos'

    id = db.Column(db.Integer, primary_key=True)
    video_url = db.Column(db.String(128))
    title = db.Column(db.String(128))
    duration = db.Column(db.String(128))
    views = db.Column(db.Integer)
    thumbnail_url = db.Column(db.String(128))
    full_image_url = db.Column(db.String(128))
    downloaded_thumbnail_path = db.Column(db.String(128))
    downloaded_full_image_path = db.Column(db.String(128))
