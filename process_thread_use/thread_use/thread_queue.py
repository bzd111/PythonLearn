# coding:utf-8
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
        print(args, task(args))
        q.task_done()


for target in (producer, consumer):
    t = threading.Thread(target=target)
    t.start()
print("ok")


# put: 向队列中添加一个项。
# get: 从队列中删除并返回一个项。
# task_done: 当某一项任务完成时调用。
# join: 阻塞直到所有的项目都被处理完。
