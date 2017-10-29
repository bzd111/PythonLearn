# coding: utf-8
from multiprocessing import cpu_count
from multiprocessing import freeze_support
from multiprocessing import Process
from multiprocessing import Queue


def apply_func(f, q_in, q_out):
    while not q_in.empty():
        i, item = q_in.get()
        q_out.put((i, f(item)))


def parmap(f, items, nprocs=cpu_count()):
    q_in, q_out = Queue(), Queue()
    proc = [Process(target=apply_func, args=(f, q_in, q_out))
            for _ in range(nprocs)]
    sent = [q_in.put((i, item)) for i, item in enumerate(items)]
    [p.start() for p in proc]
    # res = [q_out.get() for _ in sent]
    [p.join() for p in proc]
    res = [q_out.get() for _ in sent]
    return [item for _, item in sorted(res)]


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
