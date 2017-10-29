# coding:utf-8
import threading
import time
from Queue import PriorityQueue
from random import randint


q = PriorityQueue()


def double(n):
    return n * 2


def producer():
    count = 0
    while 1:
        if count > 5:
            break
        pri = randint(0, 100)
        print('put :{}'.format(pri))
        q.put((pri, double, pri))  # (priority, func, args)
        count += 1


def consumer():
    while 1:
        if q.empty():
            break
        pri, task, arg = q.get()
        print('[PRI:{}] {} * 2 = {}'.format(pri, arg, task(arg)))
        q.task_done()
        time.sleep(0.1)


t = threading.Thread(target=producer)
t.start()
time.sleep(1)
t = threading.Thread(target=consumer)
t.start()
# put :13
# put :76
# put :93
# put :86
# put :62
# put :100
# [PRI:13] 13 * 2 = 26
# [PRI:62] 62 * 2 = 124
# [PRI:76] 76 * 2 = 152
# [PRI:86] 86 * 2 = 172
# [PRI:93] 93 * 2 = 186
# [PRI:100] 100 * 2 = 200
