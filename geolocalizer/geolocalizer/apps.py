from django.apps import AppConfig
from os import getenv, path
from dotenv import load_dotenv
from geolocalizer.settings import BASE_DIR
from geolocalizer.constants import APP_NAME, ENV_FILE_NAME, IPSTACK_API_KEY


class GeolocalizerConfig(AppConfig):
    name = APP_NAME

    def ready(self):
        if not getenv(IPSTACK_API_KEY):
            env_path = path.join(BASE_DIR, APP_NAME, ENV_FILE_NAME)
            load_dotenv(dotenv_path=env_path)
