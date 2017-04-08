# -*- coding: utf-8 -*-
import unittest


class TestList(unittest.TestCase):
    def setUp(self):
        self.c_list = range(5)
        print("setup test module")

    def tearDown(self):
        del self.c_list
        print("teardown test module")

    def test_equal(self):
        print("test equal")
        c = self.c_list
        self.assertEqual(c, [0, 1, 2, 3, 4])

    def test_in(self):
        print("test in")
        c = self.c_list
        self.assertIn(1, c)


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestList("test_equal"))
    suite.addTest(TestList("test_in"))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
