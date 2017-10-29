# coding: utf-8
import multiprocessing
import time
from functools import wraps
from multiprocessing import freeze_support
from multiprocessing import pool
from multiprocessing import Process


def profile(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("cost time: {:0.2f}".format(end - start))
    return wrapper


def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


@profile
def nomultiprocess():
    fib(35)
    fib(35)
    fib(35)


@profile
def hasmultiprocess():
    jobs = []
    for i in range(3):
        p = multiprocessing.Process(target=fib, args=(35,))
        p.start()
        jobs.append(p)
    for job in jobs:
        job.join()


if __name__ == '__main__':
    freeze_support()
    nomultiprocess()
    hasmultiprocess()

# cost time: 5.52
# cost time: 2.05
