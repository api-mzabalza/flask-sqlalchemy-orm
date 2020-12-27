import os

class Config:
    SECRET_KEY = '5dff52b8ac26ff40b60afb0fb07e4e22'

    HOST_SERVER = os.environ.get('HOST_SERVER', 'localhost')
    DB_PORT = os.environ.get('DB_SERVER_PORT', '5432')
    DB_NAME = os.environ.get('DB_NAME', 'test')
    DB_USERNAME = os.environ.get('DB_USERNAME', 'mzabalza')
    DB_PASSWORD = os.environ.get('DB_PASSWORD', '123456')
    SSL_MODE='prefer'

    SQLALCHEMY_TRACK_MODIFICATIONS = True

    SQLALCHEMY_DATABASE_URI = f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{HOST_SERVER}:{DB_PORT}/{DB_NAME}?sslmode={SSL_MODE}"



