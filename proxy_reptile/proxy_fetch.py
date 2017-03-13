# coding:utf-8
import requests

import re
from mongoengine import NotUniqueError
from threading import Thread
from multiprocessing.dummy import Pool as ThreadPool
# multiprocessing.dummpy 多线程
# multiprocess 多进程
import Queue

from utils import get_user_agent
from config import TIMEOUT, PROXY_SITES, PROXY_REGEX
from models import Proxy


def fetch(url, proxy=None):

    s = requests.session()
    s.headers.update({'user-agent': get_user_agent()})
    proxies = None
    if proxy is not None:
        proxies = {'http': proxy}
    return s.get(url, timeout=TIMEOUT, proxies=proxies)


def safe_proxies(url):
    proxies = []
    try:
        r = fetch(url)
    except requests.exceptions.RequestException:
        return False
    addresses = re.findall(PROXY_REGEX, r.text)
    for address in addresses:
        print address
        proxy = Proxy(address=address)
        try:
            proxy.save()
        except NotUniqueError:
            pass
        else:
            proxies.append(address)
    return proxies


def cleanup():

    Proxy.drop_collection()


def not_thread():
    cleanup()
    for url in PROXY_SITES:
        safe_proxies(url)


def use_thread():
    cleanup()
    threads = []
    for url in PROXY_SITES:
        t = Thread(target=safe_proxies, args=(url,))
        t.setDaemon(True)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()


def use_thread_pool():

    cleanup()
    pool = ThreadPool(5)
    pool.map(safe_proxies, PROXY_SITES)
    pool.close()
    pool.join()


def safe_proxies_with_queue(queue):

    while True:
        url = queue.get()
        safe_proxies(url)
        queue.task_done()


def use_thread_with_queue():

    cleanup()
    queue = Queue.Queue()
    for i in range(5):
        t = Thread(target=safe_proxies_with_queue, args=(queue,))
        t.setDaemon(True)
        t.start()

    for url in PROXY_SITES:
        queue.put(url)

    queue.join()


def save_proxies_with_queue2(in_queue, out_queue):
    while True:
        url = in_queue.get()
        rs = safe_proxies(url)
        out_queue.put(rs)
        in_queue.task_done()


def append_result(out_queue, result):
    while True:
        rs = out_queue.get()
        if rs:
            result.extend(rs)
        out_queue.task_done()


def use_thread_with_queue2():
    cleanup()
    out_queue = Queue.Queue()
    in_queue = Queue.Queue()
    for i in range(5):
        t = Thread(target=save_proxies_with_queue2, args=(in_queue, out_queue))
        t.setDaemon(True)
        t.start()
    for url in PROXY_SITES:
        in_queue.put(url)

    result = []

    for i in range(5):
        t = Thread(target=append_result, args=(out_queue, result))
        t.setDaemon(True)
        t.start()

    in_queue.join()
    out_queue.join()

    print(len(result))
    print(result)


def show_data():
    a = Proxy.objects.all()
    for i in a:
        print(i.address,i.create_at)

if __name__ == "__main__":
    import time
    start = time.time()
    use_thread_with_queue2()
    print("Cost time:{}".format(time.time() - start))
    show_data()
