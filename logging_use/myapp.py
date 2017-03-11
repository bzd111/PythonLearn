#coding:utf-8

import mymoudle, logging
from logging import handlers

LOGNAME = "myapp.log"

log = logging.getLogger("MyApp")
log.setLevel(logging.INFO)
formatter = logging.Formatter('%(levelname)s:%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s')

ch = logging.StreamHandler()
ch.setFormatter(formatter)
log.addHandler(ch)

handler = logging.handlers.RotatingFileHandler(
    LOGNAME,
    maxBytes=10240000,  # 文件最大字节数,9.76MB
    backupCount=2,  # 会轮转2个文件，共3个
)
handler.setFormatter(formatter)
log.addHandler(handler)

log.info("Starting my app")
try:
    mymoudle.doIt()
except Exception, e:
    # log.exception("There was a problem. %s" %traceback.format_exc())
    log.exception("There was a problem.")
log.info("Ending my app")
