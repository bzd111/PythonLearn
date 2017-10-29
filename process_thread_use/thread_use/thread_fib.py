# coding=utf-8
import threading
import time
from functools import wraps
from multiprocessing import freeze_support
from multiprocessing import Pool as ProcessPool
from multiprocessing.dummy import Pool as ThreadPool


def profile(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print("{} cost:{:.2f}".format(func.__name__, end - start))
    return wrapper


def fib(n):
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)


@profile
def nothread():
    fib(5)
    fib(5)


@profile
def hasthread():
    for i in range(2):
        t = threading.Thread(target=fib, args=(5,))
        t.start()
    main_thread = threading.current_thread()
    for t in threading.enumerate():
        if t is main_thread:
            continue
        t.join()


@profile
def hasjoin():
    threads = []
    for i in range(2):
        t = threading.Thread(target=fib, args=(5,))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()


@profile
def withthreadpool():
    pool = ThreadPool(2)
    pool.map(fib, [5] * 2)


@profile
def withprocesspool():
    pool = ProcessPool(2)
    pool.map(fib, [5] * 2)


if __name__ == '__main__':
    freeze_support()
    start = time.time()
    nothread()
    hasthread()
    hasjoin()
    withthreadpool()
    withprocesspool()
    end = time.time()
    print("Total Cost {:.2f}".format(end - start))
