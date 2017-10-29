# cofing:utf-8
import threading
import time
from Queue import Queue
from random import random

q = Queue()


def double(n):
    return n * 2


def producer():
    while 1:
        wt = random()
        time.sleep(wt)
        q.put((double, wt))


def consumer():
    while 1:
        task, args = q.get()
        pritn(arg, task(args))
        q.task_done()


for target in (producer, consumer):
    t = threading.Thread(target=target)
    t.start()
