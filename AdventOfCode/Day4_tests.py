import unittest

import Day4

class Day4_tests(unittest.TestCase):
    def test_case_1(self):
        secret_key = "abcdef"
        expected = 609043
        actual = Day4.lowest_salt_with_leading_zeroes(secret_key)
        self.assertEqual(expected, actual)

    def test_case_2(self):
        secret_key = "pqrstuv"
        expected = 1048970
        actual = Day4.lowest_salt_with_leading_zeroes(secret_key)
        self.assertEqual(expected, actual)

if __name__ == '__main__':
    unittest.main(verbosity=2)
