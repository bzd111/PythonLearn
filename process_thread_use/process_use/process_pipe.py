# coding: utf-8
from multiprocessing import freeze_support
from multiprocessing import Pipe
from multiprocessing import Process


def f(conn):
    conn.send(['hello'])
    conn.close()


if __name__ == "__main__":
    freeze_support()
    parent_conn, child_con = Pipe()
    # Pipe返回的是管道2边的对象 父连接和子连接
    p = Process(target=f, args=(child_con,))
    p.start()
    print(parent_conn.recv())
    # 接收子连接发送过来的信息
    p.join()
    # 等待子进程完成
