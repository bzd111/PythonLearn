#coding:utf-8
# import logging
# import logging.handlers
#
# LOG_FILE = 'tst.log'
#
# handler = logging.handlers.RotatingFileHandler(LOG_FILE, maxBytes=1024 * 1024, backupCount=5)  # 实例化handler
# fmt = '%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s'
#
#
# formatter = logging.Formatter(fmt)  # 实例化formatter
# handler.setFormatter(formatter)  # 为handler添加formatter
#
#
# logger = logging.getLogger('tst')  # 获取名为tst的logger
# logger.addHandler(handler)  # 为logger添加handler
# logger.setLevel(logging.DEBUG)
# # ch = logging.StreamHandler()
# # ch.setFormatter(formatter)
# # logger.addHandler(ch)
# logger.debug('logger debug message')
# logger.info('logger info message')
# logger.warning('logger warning message')
# logger.error('logger error message')
# logger.critical('logger critical message')
# logger.info('first info message')
# logger.debug('first debug message')

import logging
import logging.handlers

LOGGER = logging.getLogger('Crawler')
# 设置logging模块的前缀
LOGGING_MAX_BYTES = 5 * 1024 * 1024
LOGNAME = 'test.log'
LEVELS = {  # 日志级别
    1: 'CRITICAL',
    2: 'ERROR',
    3: 'WARNING',
    4: 'INFO',
    5: 'DEBUG',  # 数字越大记录越详细
}

# formatter = logging.Formatter('%(name)s %(asctime)s %(levelname)s %(message)s')  # 自定义日志格式

formatter = logging.Formatter('%(levelname)s:%(asctime)s - %(filename)s:%(lineno)s - %(name)s - %(message)s')  # 自定义日志格式

handler = logging.handlers.RotatingFileHandler(
    LOGNAME,
    maxBytes=10240000,  # 文件最大字节数
    backupCount=2,  # 会轮转5个文件，共6个
)
handler.setFormatter(formatter)  # 设置日志格式
LOGGER.addHandler(handler)  # 增加处理器
logger = logging.getLogger('test1')
logger.setLevel(logging.INFO)
logger.addHandler(handler)

ch = logging.StreamHandler()
ch.setFormatter(formatter)
logger.addHandler(ch)
while True:
    logger.info('logger info message')
    logger.warning('logger warning message')
    logger.error('logger error message')
    logger.critical('logger critical message')
    logger.info('first info message')
    logger.debug('first debug message')

	

def configLogger(logfile):
    '''配置日志文件和记录等级'''
    try:
        handler = logging.handlers.RotatingFileHandler(logfile,
                                                       maxBytes=10240000,  # 文件最大字节数
                                                       backupCount=5,  # 会轮转5个文件，共6个
                                                       )
    except IOError, e:
        print
        e
        return -1
    else:
        handler.setFormatter(formatter)  # 设置日志格式
        LOGGER.addHandler(handler)  # 增加处理器
        logging.basicConfig(level=logging.NOTSET)  # 设置,不打印小于4级别的日志
    return LOGGER  # 返回logging实例


def myLogger(logger, lv, mes, err=False):
    '''记录日志函数'''
    getattr(logger, LEVELS.get(lv, 'WARNING').lower())(mes)
    if err:  # 当发现是错误日志,还会记录错误的堆栈信息
        getattr(logger, LEVELS.get(lv, 'WARNING').lower())(traceback.format_exc())
