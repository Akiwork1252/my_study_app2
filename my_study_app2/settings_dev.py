from .settings_common import *

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = []

# ロギング
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'INFO',
        },
        'ascension': {
            'handlers': ['console'],
            'level': 'DEBUG',
        }
    },

    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'dev',
        }
    },

    'formatters': {
        'dev': {
            'format': '\t'.join([
                '%(asctime)s',
                '%(levelname)s',
                '%(pathname)s(Line:%(lineno)d)',
                '%(message)s',
            ])
        }
    },
}

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
