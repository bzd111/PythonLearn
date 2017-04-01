# -*- coding: utf-8 -*-
import unittest
from collections import Counter


def setUpModule():
    print("setup module")


def tearDownModule():
    print("teardown module")


class TestCounter(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("First running print")

    def setUp(self):
        self.c = Counter("aaabbcd")
        print("setup test module")

    def tearDown(self):
        del self.c
        print("teardown test module")

    def test_baisc(self):
        c = self.c
        self.assertEqual(c, Counter(a=3, b=2, c=1, d=1))
        self.assertIn('a', c)
        self.assertNotIn('f', c)
        self.assertIsInstance(c, dict)
        self.assertEqual(len(c), 4)

    def test_update(self):
        c = self.c
        c.update(f=1)
        self.assertEqual(c, Counter(a=3, b=2, c=1, d=1, f=1))
        c.update(a=10)
        self.assertEqual(c, Counter(a=13, b=2, c=1, d=1, f=1))

    @classmethod
    def tearDownClass(cls):
        print("last running print")
# if __name__=="__main__":
#     unittest.main()


if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(TestCounter("test_baisc"))  # 通过任务添加
    suite.addTest(TestCounter("test_update"))
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
