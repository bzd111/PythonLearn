#!/usr/bin/env python
# -*- coding:utf-8 -*-
from Base import get_linkedlist


def first_same(phead1, phead2):
    pcur1 = phead1.next
    pcur2 = phead2.next
    length1 = len(pcur1)
    length2 = len(pcur2)
    if length1 < length2:
        pcur1, pcur2 = pcur2, pcur1
    for i in range(abs(length2 - length1)):
        pcur1 = pcur1.next
    while pcur1:
        # TODO
        if pcur1 == pcur2:
            return pcur1
        pcur1 = pcur1.next
        pcur2 = pcur2.next


if __name__ == '__main__':
    pcommon = get_linkedlist(2)
    print(pcommon)
    phead1, tail1 = get_linkedlist(10, with_tail=True)
    print(phead1)
    print(tail1)
    phead2, tail2 = get_linkedlist(8, with_tail=True)
    print(phead2)
    print(tail2)
    tail1.next = pcommon.next
    tail2.next = pcommon.next
    print(phead1, phead2)
    print(first_same(phead1, phead2))

