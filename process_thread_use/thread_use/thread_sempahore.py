# coding: utf-8
import time
from random import random
from threading import Semaphore
from threading import Thread

sema = Semaphore(3)


def foo(tid):
    with sema:
        print("{} acquire sema".format(tid))
        wt = random() * 2
        time.sleep(wt)
    print("{} release sema.".format(tid))


threads = []

for i in range(5):
    t = Thread(target=foo, args=(i, ))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

# 0 acquire sema
# 1 acquire sema
# 2 acquire sema
# 2 release sema.
# 3 acquire sema
# 0 release sema.
# 4 acquire sema
# 4 release sema.
# 1 release sema.
# 3 release sema.
