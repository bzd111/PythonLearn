#!/usr/bin/env python
# -*- coding:utf-8 -*-
from Base import Node, get_linkedlist


def split(phead, x):
    pcur1 = p1 = Node(0)
    pcur2 = p2 = Node(0)
    pcur = phead.next
    while pcur:
        if pcur._value < x:
            pcur1.next = pcur
            # pcur1 = pcur
            pcur1 = pcur1.next
        else:
            pcur2.next = pcur
            # pcur2 = pcur
            pcur2 = pcur2.next
        pcur = pcur.next
    pcur1.next = p2.next
    pcur2.next = None
    phead.next = p1.next


if __name__ == '__main__':
    phead = get_linkedlist(10)
    print(phead)
    split(phead, 5)
    print(phead)


