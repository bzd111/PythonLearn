from threading import Thread
from  Queue import Queue
from random import random


def Produce(queue):
    for _ in range(10):
        put_x = random() * 5
        print("Procude x is:%s" % put_x)
        queue.put(put_x)


def Consumer(queue):
    while True:
        get_x = queue.get()
        print("Consumer x is:%s" % get_x)
        queue.task_done()


q = Queue()
t1 = Thread(target=Produce, args=(q,))
t2 = Thread(target=Consumer, args=(q,))
t1.start()
t2.start()