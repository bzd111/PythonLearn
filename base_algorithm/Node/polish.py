#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import division

def reversed_polish(notation):
    stack = []
    for token in notation:
        if token not in '+-*/':
            stack.append(token)
        else:
            b = stack.pop()
            a = stack.pop()
            # value = eval('{}{}{}'.format(a, token, b))

            a, b = ((a, b), ('(' + a, b + ')'))[token in '+-']
            value = '{}{}{}'.format(a, token, b)
            stack.append(value)
    express = stack.pop()
    return express, eval(express)


if __name__ == '__main__':
    for notation in [['2', '1', '+', '3', '*'],
                     ['4', '13', '5', '/', '+']]:
        print(notation, reversed_polish(notation))

