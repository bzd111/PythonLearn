#!/usr/bin/env python
# -*- coding:utf-8 -*-
from random import randint


class Node(object):

    """Docstring for Node. """

    def __init__(self, value):
        """TODO: to be defined1.

        Args:
            value (TODO): TODO


        """
        self._value = value
        self.next = None

    def __len__(self):
        length = 1
        p = self
        while p.next:
            length += 1
            p = p.next
        return length

    def __str__(self):
        p = self
        if not p:
            return ''
        output = str(p._value)
        while p.next:
            output += '->{}'.format(p.next._value)
            p = p.next
        return output

    def __bool__(self):
        return self is not Node


def get_linkedlist(length, maxint=9, with_tail=False):
    """ return linkedlist """
    pcur = phead = Node(0)
    for i in range(length):
        pcur.next = Node(randint(0, maxint))
        pcur = pcur.next
    if with_tail:
        return phead, pcur
    return phead


if __name__ == '__main__':
    pass


