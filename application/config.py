import os

class Config:
    SECRET_KEY = '2ff0405a48a5b9094df11272478c894f'
    SQLALCHEMY_DATABASE_URI = os.getenv('DEV_SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Disable modification tracking
    DEBUG = True  # Set to True for development, False for production
