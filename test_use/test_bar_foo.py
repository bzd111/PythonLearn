# -*- coding: utf-8 -*-

import unittest


class TestFoo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("foo setup class ")

    @classmethod
    def tearDownClass(cls):
        print("foo teardown class")

    def setUp(self):
        print("foo setup")

    def tearDown(self):
        print("foo teardown")

    def test_baisc(self):
        self.assertTrue(True)


class TestBar(unittest.TestCase):

    def setUp(self):
        print('bar setup')

    def tearDown(self):
        print('bar teardown')

    def test_baisc(self):
        self.assertTrue(True)
