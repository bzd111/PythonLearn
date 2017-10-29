# coding: utf-8
import time
from functools import wraps
from multiprocessing import freeze_support
from multiprocessing import Pool  # 导入的是多进程池


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
def hasmultiprocesspool():
    pool = Pool(3)
    pool.map(fib, [35] * 3)


if __name__ == '__main__':
    freeze_support()
    nomultiprocess()
    hasmultiprocesspool()

# cost time: 5.51
# cost time: 1.9
