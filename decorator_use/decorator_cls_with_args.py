# -*- coding: utf-8 -*-


class decorate_args_class(object):
    def __init__(self, name):
        self.name = name

    def __call__(self, func):
        def warp(*args, **kwargs):
            print('{} say:'.format(self.name))
            return func(*args, **kwargs)
        return warp


@decorate_args_class(name='zxc')
def say_hello(what):
    return '{:>13}'.format(what)


def say_hello_none(what):
    return '{:>13}'.format(what)


class TestSay(object):

    @decorate_args_class(name='zidy')
    def say_hello(self, what):
        return '{:>13}'.format(what)


if __name__ == "__main__":

    print(say_hello('hello'))
    print("-"*30)
    d_a_class = decorate_args_class(name='zxc')
    print(d_a_class(say_hello_none)('hello'))
    print("-"*30)
    a = TestSay()
    print(a.say_hello('hello'))
