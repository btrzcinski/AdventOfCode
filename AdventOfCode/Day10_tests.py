import unittest

import Day10

class Day10_tests(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual("11", Day10.lookandsay("1", reps=1))

    def test_case_11(self):
        self.assertEqual("21", Day10.lookandsay("11", reps=1))

    def test_case_21(self):
        self.assertEqual("1211", Day10.lookandsay("21", reps=1))

    def test_case_1211(self):
        self.assertEqual("111221", Day10.lookandsay("1211", reps=1))

    def test_case_111221(self):
        self.assertEqual("312211", Day10.lookandsay("111221", reps=1))

    def test_case_1_5x(self):
        self.assertEqual("312211", Day10.lookandsay("1", reps=5))

if __name__ == '__main__':
    unittest.main()
