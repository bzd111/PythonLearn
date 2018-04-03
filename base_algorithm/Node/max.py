#!/usr/bin/env python
# -*- coding:utf-8 -*-
def match_parentheses_maxlength(s):
    maxlength = 0
    start = -1
    stack = []
    for i, c in enumerate(s):
        if c == '(':
            stack.append(i)
        else:
            if not stack:
                start = i
            else:
                stack.pop()
                if not stack:
                    maxlength = max(maxlength, i - start)
                else:
                    maxlength = max(maxlength, i - stack[-1])
    return maxlength


if __name__ == '__main__':
    for s in ['(()', '()()', '()(())', '(()()))']:
        print(s, match_parentheses_maxlength(s))

