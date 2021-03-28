from .settings import *

INSTALLED_APPS.append('debug_toolbar')
INSTALLED_APPS.append('corsheaders')

MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')
MIDDLEWARE.append('corsheaders.middleware.CorsMiddleware')

INTERNAL_IPS = ['127.0.0.1', 'localhost']

DEBUG = True

if DEBUG:
    ALLOWED_HOSTS += ["127.0.0.1", "localhost"]

    STATIC_ROOT = None
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static/')
    ]

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_CREDENTIALS = True


if DEBUG:
    ALLOWED_HOSTS += ["localhost"]

    STATIC_ROOT = None
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static/')
    ]


# EMAIL_BACKEND = 'django.core.mail.backends.localmem.EmailBackend'

CORS_ORIGIN_ALLOW_ALL = True

CORS_ALLOW_CREDENTIALS = True