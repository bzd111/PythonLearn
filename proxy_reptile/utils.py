# -*- coding: utf-8 -*-
import random
from fake_useragent import UserAgent

from config import REFERER_LIST


def get_referer():
    return random.choice(REFERER_LIST)


def get_user_agent():

    ua = UserAgent()
    return ua.random
