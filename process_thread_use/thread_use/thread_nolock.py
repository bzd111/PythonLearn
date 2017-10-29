# coding: utf-8
import time
from threading import Thread

value = 0


def getlock():
    global value
    new = value + 1
    time.sleep(0.001)
    value = new


threads = []

for i in range(100):
    t = Thread(target=getlock)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print(value)
print("OK")
