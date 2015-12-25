import unittest

import Day20

class Day20_tests(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(1, Day20.lowest_numbered_house_to_get_presents(10))

    def test_example_2(self):
        self.assertEqual(2, Day20.lowest_numbered_house_to_get_presents(30))

    def test_example_4(self):
        self.assertEqual(4, Day20.lowest_numbered_house_to_get_presents(70))

if __name__ == "__main__":
    unittest.main(verbosity=2)
