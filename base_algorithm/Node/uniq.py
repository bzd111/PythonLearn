#!/usr/bin/env python
# -*- coding:utf-8 -*-
from Base import get_linkedlist


def uniq(phead):
    pcur = phead.next
    while pcur:
        pnext = pcur.next
        if not pnext:
            return
        if pcur._value == pnext._value:
            pcur.next = pnext.next
        pcur = pcur.next


if __name__ == '__main__':
    phead = get_linkedlist(20, maxint=5)
    print(phead)
    uniq(phead)
    print(phead)

