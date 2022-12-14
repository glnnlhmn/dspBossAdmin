from decouple import config


def str_to_bool(s: str) -> bool:
    return s.upper() == "TRUE"


class Config:
    DB_HOST = config('DB_HOST')
    DB_NAME = config('DB_NAME')
    DB_PORT = config('DB_PORT')
    DB_USER = config('DB_USER')
    DB_PASSWORD = config('DB_PASSWORD')
    DB_AUTOCOMMIT = True

    SQLALCHEMY_DATABASE_URI = config('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_ECHO = config('SQLALCHEMY_ECHO')
    SQLALCHEMY_TRACK_MODIFICATIONS = config('SQLALCHEMY_TRACK_MODIFICATIONS')
    SECRET_KEY = config('SECRET_KEY')

    DSPBOSS_ADMIN_MODE = str_to_bool(config('DSPBOSS_ADMIN_MODE'))

    FLASK_ADMIN_SWATCH = config('FLASK_ADMIN_SWATCH')

    SECURITY_PASSWORD_SALT = config('SECURITY_PASSWORD_SALT')

    DEBUG = config('DEBUG')
