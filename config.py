from os import environ, os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):

    POSTGRES = {
        'user': 'postgres',
        'pw': '',
        'db': 'youtube',
        'host': 'postgresql',
        'port': '5432',
    }

    # Database
    SQLALCHEMY_DATABASE_URI = 'postgresql://%(user)s:\%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

    SQLALCHEMY_TRACK_MODIFICATIONS = False
