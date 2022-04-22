from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=["settings.toml", ".secrets.toml"],
)

NAME = settings.APP.NAME
HOST = settings.APP.HOST
PORT = settings.APP.PORT
VERSION = settings.APP.VERSION
HOMEPAGE = settings.APP.HOMEPAGE

SECRET_TOKEN = settings.get("SECRET", "secret-phrase")
DATA_PATH = "data.json"
