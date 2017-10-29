# coding: utf-8
import time
from multiprocessing import freeze_support
from multiprocessing import JoinableQueue
from multiprocessing import Process
from multiprocessing import Queue
from random import random
# 进程的Queue类并不支持task_done和join方法，需要使用特别的JoinableQueue

tasks_queue = JoinableQueue()
results_queue = Queue()


def double(n):
    return n * 2


def producer(in_queue):
    while 1:
        wt = random()
        time.sleep(wt)
        in_queue.put((double, wt))
        if wt > 0.9:
            in_queue.put(None)
            print("Stop Producer")
            break


def consumer(in_queue, out_queue):
    while 1:
        task = in_queue.get()
        if task is None:
            break
        func, args = task
        result = func(args)
        in_queue.task_done()
        out_queue.put(result)


if __name__ == "__main__":
    freeze_support()
    processes = []

    p = Process(target=producer, args=(tasks_queue,))
    p.start()
    processes.append(p)

    p = Process(target=consumer, args=(tasks_queue, results_queue))
    p.start()
    processes.append(p)

    tasks_queue.join()

    for p in processes:
        p.join()

    while 1:
        if results_queue.empty():
            break
        result = results_queue.get()
        print("Result: ", result)
