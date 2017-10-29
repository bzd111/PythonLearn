# coding: utf-8
import threading
import time
from Queue import Queue
from random import random


def double(n):
    return [_ * 2 for _ in n]


class Worker(threading.Thread):
    def __init__(self, queue):
        super(Worker, self).__init__()
        self._q = queue
        self.daemon = True
        self.start()

    def run(self):
        while 1:
            f, args, kwargs = self._q.get()
            try:
                print("use: {}".format(self.name))
                print(f(*args, **kwargs))
            except Exception as e:
                print(e)
            self._q.task_done()


class ThreadPool(object):
    def __init__(self, num_t=5):
        self._q = Queue(num_t)
        for _ in range(num_t):
            Worker(self._q)

    def add_task(self, f, *args, **kwargs):
        self._q.put((f, args, kwargs))

    def wait_complete(self):
        self._q.join()


pool = ThreadPool()
for _ in range(8):
    wt = random()
    pool.add_task(double, range(5))
    time.sleep(wt)
pool.wait_complete()
