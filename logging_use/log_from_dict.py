import logging
from logging.config import fileConfig,dictConfig
import yaml
import os
import mymoudle, logging , logging.handlers
import  simplejson as json

def setup_logging(
    default_path='log1.yaml',
    default_level=logging.INFO,
    env_key='LOG_CFG'
):
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as f:
            config = yaml.safe_load(f.read())
            # print(type(config))
            # with open('log.json','w') as f1:
            #     json.dump(config,f1)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

setup_logging()
log = logging.getLogger("MyApp")


log.info("Starting my app")
try:
    mymoudle.doIt()
except Exception, e:
    # log.exception("There was a problem. %s" %traceback.format_exc())
    log.exception("There was a problem.")
log.info("Ending my app")
