import os

class Config:
    SECRET_KEY = "tempsecretkey"
    SQLALCHEMY_DATABASE_URI = "sqlite:///site.db"
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = "email here or use os.environ"
    MAIL_PASSWORD = "password for email here or use os.environ"