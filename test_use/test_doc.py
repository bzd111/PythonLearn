# -*- coding: utf-8 -*-


def double(num):
    """ This function calculate positive integer square value.

    Example:

        >>> double(10)
        100
        >>> double(-1)
        Traceback (most recent call last):
        ...
        ValueError: the num must is positive integer
    """

    if num < 0:
        raise ValueError('the num must is positive integer')
    return num**2


if __name__ == "__main__":
    import doctest
    doctest.testmod()
