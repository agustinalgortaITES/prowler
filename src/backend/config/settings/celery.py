from config.env import env

VALKEY_HOST = env("VALKEY_HOST", default="valkey-db")
VALKEY_PORT = env("VALKEY_PORT", default="6479")
VALKEY_DB = env("VALKEY_DB", default="0")

CELERY_BROKER_URL = f"redis://{VALKEY_HOST}:{VALKEY_PORT}/{VALKEY_DB}"
CELERY_RESULT_BACKEND = "django-db"

CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP = True
