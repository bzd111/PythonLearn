# coding:utf-8
import logging
import logging.config
import os
import sys

import mymoudle

LOG_DIR = os.path.dirname(__file__)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format':
            '[%(levelname)s][%(asctime)s][%(module)s][%(process)d] %(message)s',
        },
        'module': {
            'format': '[%(levelname)s][%(asctime)s][%(process)d] %(message)s',
        },
        'simple': {
            'format': '%(message)s',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'stream': sys.stdout,
        },
        'app': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'app.log'),
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
            'formatter': 'module',
        },
        'module': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'module_dict.log'),
            'maxBytes': 1024 * 1024 * 5,  # 5 MB
            'backupCount': 5,
            'formatter': 'module',
        },


    },
    'loggers': {
        'app': {
            'handlers': ['console', 'app'],
            'level': 'INFO',
            'propagate': False,
        },
        'Mymoudle': {
            'handlers': ['console', 'module'],
            'level': 'INFO',
            'propagate': False,
        },
    },
}

logging.config.dictConfig(LOGGING)

log = logging.getLogger('app')
try:
    mymoudle.doIt()
except Exception as e:
    # log.exception("There was a problem. %s" %traceback.format_exc())
    log.exception("There was a problem.")
log.info("Ending my app")
