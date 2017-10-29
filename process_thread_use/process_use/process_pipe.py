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
    # Pipe���ص��ǹܵ�2�ߵĶ��� �����Ӻ�������
    p = Process(target=f, args=(child_con,))
    p.start()
    print(parent_conn.recv())
    # ���������ӷ��͹�������Ϣ
    p.join()
    # �ȴ��ӽ������
