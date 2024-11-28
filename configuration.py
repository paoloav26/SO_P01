import os
from dotenv import load_dotenv

load_dotenv()


class Config():
    # FLASK CONFIG
    SECRET_KEY = os.getenv('SECRET_KEY')
    PROPAGATE_EXCEPTIONS = False

    # BD CONFIG

    # FLASK MAIL CONFIG
    #MAIL_SERVER = os.getenv('MAIL_SERVER')
    #MAIL_PORT = os.getenv('MAIL_PORT')
    #MAIL_USERNAME = os.getenv('MAIL_USERNAME')
    #MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')
    #MAIL_USE_TLS = True
    #MAIL_USE_SSL = False

class DevConfig(Config):
    DEBUG=True


class TestingConfig(Config):
    TESTING = True

class Production(Config):
    DEBUG=False