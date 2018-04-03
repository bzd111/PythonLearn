#!/usr/bin/env python
# -*- coding:utf-8 -*-
from Base import get_linkedlist


def reverse(phead, m, n):
    pcur = phead
    for i in range(0, m-1):
        pcur = pcur.next
    print(pcur._value)
    ppre = pcur
    pcur = pcur.next
    for i in range(m, n):
        pnext = pcur.next
        pcur.next = pnext.next
        pnext.next = ppre.next
        ppre.next = pnext


if __name__ == '__main__':
    phead = get_linkedlist(10)
    print(phead)
    reverse(phead, 3, 8)
    print(phead)


