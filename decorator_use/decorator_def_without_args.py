# -*- coding: utf-8 -*-
from functools import wraps


def decorate_test(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        print('This is a decorate')
        print('func name {}'.format(func.__name__))
        return func(*args, **kwargs)
    return wrap


@decorate_test
def say_hello():
    return 'say hello'


def say_hello_none():
    return 'say hello'


class TestSay(object):

    @decorate_test
    def say_hello(self):
        return 'say hello'


if __name__ == "__main__":
    print(say_hello())
    print("-"*30)
    print(decorate_test(say_hello_none)())
    print("-"*30)
    test = TestSay()
    print(test.say_hello())
