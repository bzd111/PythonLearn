# coding=utf-8
import threading
import time

condition = threading.Condition()


def consumer(cond):
    t = threading.current_thread()
    with cond:
        cond.wait()  # wait()方法创建了一个名为waiter的锁，并且设置锁的状态为locked。这个waiter锁用于线程间的通讯
        print("{}: Resource is available to consumer".format(t.name))


def producer(cond):
    t = threading.current_thread()
    with cond:
        print("{}: Making resource acailable".format(t.name))
        cond.notifyAll()  # 释放waiter锁，唤醒消费者


c1 = threading.Thread(target=consumer, args=(condition, ), name="c1")
c2 = threading.Thread(target=consumer, args=(condition, ), name="c2")
p1 = threading.Thread(target=producer, args=(condition, ), name="p1")

c1.start()
time.sleep(1)
c2.start()
time.sleep(1)
p1.start()
p1.join()
c1.join()
c2.join()
print("ok")
