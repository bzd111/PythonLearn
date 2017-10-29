# coding: utf-8
from multiprocessing import Manager
from multiprocessing import Process


def modify(ns, lproxy, dproxy):
    ns.a **= 2
    lproxy.extend(['b', 'c'])
    dproxy['b'] = 0


manager = Manager()
ns = manager.Namespace()

ns.a = 1
lproxy = manager.list()
lproxy.append('a')
dproxy = manager.dict()
dproxy['b'] = 2
p = Process(target=modify, args=(ns, lproxy, dproxy))
p.start()
print 'PID:', p.pid
p.join()
print ns.a
print lproxy
print dproxy

# �����Ĺ���ʽ�����¼��֣�
# Namespace������һ���ɷ���������ռ䡣
# Value/Array�������湲��ctypes����ķ�ʽһ����
# dict/list������һ���ɷ����dict/list��֧�ֶ�Ӧ���ݽṹ�ķ�����
# Condition/Event/Lock/Queue/Semaphore������һ���ɷ���Ķ�Ӧͬ��ԭ��Ķ���
