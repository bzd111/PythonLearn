# -*- coding: utf-8 -*-
import unittest
SKIP = False


class TestList(unittest.TestCase):
    def setUp(self):
        self.c_list = range(5)
        print("setup test module")

    def tearDown(self):
        del self.c_list
        print("teardown test module")

    @unittest.skip("skip this test")
    def test_equal(self):
        print("test equal")
        c = self.c_list
        self.assertEqual(c, [0, 1, 2, 3, 4])

    @unittest.skipIf(SKIP is True, "skip this test with if")
    def test_in(self):
        print("test in")
        c = self.c_list
        self.assertIn(1, c)


if __name__ == "__main__":
    unittest.main()
