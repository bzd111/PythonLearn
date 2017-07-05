# -*- coding: utf-8 -*-
import re


DB_HOST = '10.1.10.68'
DB_PORT = 27017
DATABASE_NAME = 'urls'

TIMEOUT = 10

PROXY_SITES = [
    "http://www.66ip.cn/",
    'http://cn-proxy.com',
    'http://www.xicidaili.com',
    'http://www.kuaidaili.com/free',
    'http://www.proxylists.net/?HTTP',
    # www.youdaili.net的地址随着日期不断更新
    'http://www.youdaili.net/Daili/http/4565.html',
    'http://www.youdaili.net/Daili/http/4562.html',
    'http://www.kuaidaili.com',
    'http://proxy.mimvp.com'
]

REFERER_LIST = [
    'http://www.baidu.com',
    'http://www.google.com'
]

PROXY_REGEX = re.compile('[0-9]+(?:\.[0-9]+){3}:\d{2,4}')
