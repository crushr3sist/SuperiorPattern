class Config(object):
    SQLALCHEMY_DATABASE_URI = "sqlite:///database.sqlite"
    SECRET_KEY = "xxxxyyyyyzzzzz"


class Production(Config):
    DEBUG = False


class Development(Config):
    DEBUG = True
    TESTING = True
