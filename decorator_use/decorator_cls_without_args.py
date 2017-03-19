# -*- coding: utf-8 -*-


class decorate_class(object):
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):

        print('This is a class decorate')
        return self.func(*args, **kwargs)

    def __get__(self, instance, owner):

        return lambda *args, **kwargs: self.func(instance, *args, **kwargs)


@decorate_class
def say_hello(what):
    return 'say {}'.format(what)


def say_hello_none(what):
    return 'say {}'.format(what)


class TestSay(object):

    @decorate_class
    def say_hello(self, what):
        return 'say {}'.format(what)


if __name__ == "__main__":
    print(say_hello('hello'))

    print("-"*30)
    print(decorate_class(say_hello_none)('hello'))

    print("-"*30)
    test = TestSay()
    print(test.say_hello("hello"))
