#!/usr/bin/env python
# -*- coding:utf-8 -*-
def stack_inout_possiable(in_seq, out_seq):
    stack = []
    i = j = 0
    length = len(in_seq)
    while j < length:
        # TODO
        if stack and out_seq[j] == stack[-1]:
            stack.pop()
            j += 1
        else:
            if i == length:
                return False
            stack.append(in_seq[i])
            i += 1
    return not stack

if __name__ == '__main__':
    print(stack_inout_possiable('ABCDEFG', 'BAEDFGC'))
    print(stack_inout_possiable('ABCD', 'BDAC'))

