import os

from dotenv import load_dotenv
from pathlib import Path
from split_settings.tools import include

load_dotenv()

include(
    'components/database.py',
    'components/middleware.py',
    'components/templates.py',
    'components/installed_apps.py',
    'components/auth_password_validators.py',
)

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = os.environ.get('DEBUG')

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '127.0.0.1').split(' ')

if DEBUG:
    import socket
    INTERNAL_IPS = ['127.0.0.1',]
    hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
    INTERNAL_IPS = [ip[: ip.rfind(".")] + ".1" for ip in ips] + ["127.0.0.1", "10.0.2.2"]

ROOT_URLCONF = 'example.urls'

WSGI_APPLICATION = 'example.wsgi.application'

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = ['movies/locale']

STATIC_URL = '/static/'
