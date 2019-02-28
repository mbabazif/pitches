import os


class Config:

    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wecode:mba123456@localhost/pitches'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'

    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    @staticmethod
    def init_app(app):
        SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
        pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True


config_options = {'development': DevConfig, 'production': ProdConfig}
