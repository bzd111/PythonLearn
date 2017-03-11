#coding:utf-8

import logging
log = logging.getLogger("Mymoudle")

def doIt():
        log.debug("Doin' stuff...")
        #do stuff...
        raise TypeError, "Bogus type error for testing"