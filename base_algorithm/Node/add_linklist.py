#!/usr/bin/env python
# -*- coding:utf-8 -*-
from Base import Node, get_linkedlist


def add(phead1, phead2):
    psum = Node(0)
    ptail = psum
    p1 = phead1.next
    p2 = phead2.next
    carry = 0
    while p1 and p2:
        value = p1._value + p2._value + carry
        carry = value // 10
        value %= 10
        ptail.next = Node(value)
        ptail= ptail.next
        p1 = p1.next
        p2 = p2.next
    p = p1 if p1 else p2
    while p:
        value = p._value + carry
        carry = value // 10
        ptail.next = Node(value)
        ptail = ptail.next
        p = p.next
    if carry:
        ptail.next = Node(carry)
    return psum

if __name__ == '__main__':
    phead1 = get_linkedlist(5)
    phead2 = get_linkedlist(8)
    print(phead1)
    print(phead2)
    psum = add(phead1, phead2)
    print(psum)

