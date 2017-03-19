# -*- coding: utf-8 -*-
from functools import wraps


def decorate_args(name):
    def warp(func):
        @wraps(func)
        def warp_func(*args, **kwargs):
            print('{} say:'.format(name))
            return func(*args, **kwargs)

        return warp_func

    return warp


@decorate_args(name='zxc')
def say_hello():
    return '      hello'


def say_hello_none():
    return '      hello'


class TestSay(object):
    @decorate_args(name='zxc')
    def say_hello(self):
        return '      hello'


if __name__ == "__main__":
    print(say_hello())
    print("-"*30)
    print(decorate_args(name='zcx')(say_hello_none)())
    print("-"*30)
    test = TestSay()
    print(test.say_hello())
