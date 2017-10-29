# coding=utf-8
import threading
import time

condition = threading.Condition()


def consumer(cond):
    t = threading.current_thread()
    with cond:
        cond.wait()  # wait()����������һ����Ϊwaiter������������������״̬Ϊlocked�����waiter�������̼߳��ͨѶ
        print("{}: Resource is available to consumer".format(t.name))


def producer(cond):
    t = threading.current_thread()
    with cond:
        print("{}: Making resource acailable".format(t.name))
        cond.notifyAll()  # �ͷ�waiter��������������


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
