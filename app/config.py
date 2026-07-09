
import os

from dotenv import load_dotenv

load_dotenv()

APP_NAME = os.getenv("APP_NAME")

APP_VERSION = os.getenv("APP_VERSION")

APP_ENV = os.getenv("APP_ENV")

APP_DEBUG = os.getenv("APP_DEBUG")

DB_DRIVER = os.getenv("DB_DRIVER")

DB_SERVER = os.getenv("DB_SERVER")

DB_DATABASE = os.getenv("DB_DATABASE")

DB_AUTH_MODE = os.getenv("DB_AUTH_MODE")

DB_USERNAME = os.getenv("DB_USERNAME")

DB_PASSWORD = os.getenv("DB_PASSWORD")

DB_ENCRYPT = os.getenv("DB_ENCRYPT")

DB_TRUST_SERVER_CERTIFICATE = os.getenv("DB_TRUST_SERVER_CERTIFICATE")

DEFAULT_PAGE_SIZE = os.getenv("DEFAULT_PAGE_SIZE")

MAX_PAGE_SIZE = os.getenv("MAX_PAGE_SIZE")

