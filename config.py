#-------------------------------------- https://github.com/XNKIT ------------------------------------------#
import os

class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5629704176:AAELzqoqEeSjrH74CDeujYXC-UVv9dALgXk")
    APP_ID = int(os.environ.get("APP_ID"), "16596628")
    API_HASH = os.environ.get("API_HASH"), "421764a823ee2dff786d413aea09959f")
    ADMIN = int(os.environ.get("ADMIN"), "5556908572")
