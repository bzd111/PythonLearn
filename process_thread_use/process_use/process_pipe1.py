# coding: utf-8
from itertools import izip
from multiprocessing import freeze_support
from multiprocessing import Pipe
from multiprocessing import Pool
from multiprocessing import Process


def spawn(f):
    def func(pipe, item):
        pipe.send(f(item))
        pipe.close()
    return func


def parmap(f, items):
    pipe = [Pipe() for _ in items]
    proc = [
        Process(
            target=spawn(f),
            args=(child, item),
        )
        for item, (parent, child) in izip(items, pipe)
    ]
    [p.start() for p in proc]
    [p.join() for p in proc]
    return [parent.recv() for (parent, child) in pipe]


class CalculateFib(object):
    @classmethod
    def fib(cls, n):
        if n <= 2:
            return 1
        return cls.fib(n - 1) + cls.fib(n - 2)

    def map_run(self):
        pool = Pool(2)
        print(pool.map(self.fib, [35] * 2))

    def parmp_run(self):
        print(parmap(self.fib, [35] * 2))


if __name__ == "__main__":
    freeze_support()
    cal = CalculateFib()
    cal.parmp_run()
