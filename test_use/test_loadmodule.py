# -*- coding: utf-8 -*-
import unittest

from test_bar_foo import TestBar, TestFoo
import test_bar_foo


def setUpModule():
    print("setup module")


def tearDownModule():
    print("teardown module")


if __name__ == "__main__":
    test_bar_foo.setUpModule = setUpModule
    test_bar_foo.tearDownModule = tearDownModule
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestBar)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(TestFoo)
    suites = unittest.TestSuite([suite1, suite2])
    unittest.TextTestRunner().run(suites)
