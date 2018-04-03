#!/usr/bin/env python
# -*- coding:utf-8 -*-
parentheses_map = {
    '(': ')',
    '[': ']',
    '{': '}'
}


def match_parentheses(s):
    stack = []
    for c in s:
        if c in '([{':
            stack.append(c)
        else:
            if not stack or parentheses_map[stack[-1]] != c:
                return False
            stack.pop()
    return not stack


if __name__ == '__main__':
    s = '(({})[])[()]'
    print(s, match_parentheses(s))
    s = '(({)[])[()]'
    print(s, match_parentheses(s))
