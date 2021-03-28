from .settings import *

DEBUG = False

ADMINS = [(env('ADMIN_FULL_NAME'), env('ADMIN_EMAIL'))]

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'verbose': {
            'format': '----------------------------\n'
                      '%(levelname)s: %(asctime)s: %(module)s: %(filename)s:%(funcName)s:%(lineno)d\n'
                      '%(message)s \n\n'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
        },
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'errors-customer-feedback.log',
            'maxBytes': 5*1024*1024,  # 5 MB
            'backupCount': 5,  # 5 logs max
            'formatter': 'verbose'
        },
        'schema': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'schema_changes.log',
            'formatter': 'verbose'
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['file', 'mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.server': {
            'handlers': ['file', 'mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'django.db.backends.schema': {
            'handlers': ['schema', 'mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'custom_logger': {
            'handlers': ['file', 'mail_admins'],
            'level': 'INFO',
        }
    }
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
