import logging
from logging.config import fileConfig,dictConfig

# fileConfig('log.ini')
# logger = logging.getLogger()
# logger.debug('often makes a very good meal of %s', 'visiting tourists')


#coding:utf-8

import mymoudle, logging , logging.handlers
import traceback


LOGNAME = "myapp.log"

fileConfig('log.ini')
log = logging.getLogger("MyApp")
log.setLevel(logging.INFO)

log.info("Starting my app")
try:
    mymoudle.doIt()
except Exception, e:
    # log.exception("There was a problem. %s" %traceback.format_exc())
    log.exception("There was a problem.")
log.info("Ending my app")
