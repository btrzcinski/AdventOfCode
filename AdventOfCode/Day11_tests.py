import unittest

import Day11

class Day11_tests(unittest.TestCase):
    def test_is_valid_hijklmmn(self):
        self.assertFalse(Day11.is_valid_password("hijklmmn"))

    def test_is_valid_abbceffg(self):
        self.assertFalse(Day11.is_valid_password("abbceffg"))

    def test_is_valid_abbcegjk(self):
        self.assertFalse(Day11.is_valid_password("abbcegjk"))

    def test_is_valid_abcdffaa(self):
        self.assertTrue(Day11.is_valid_password("abcdffaa"))

    def test_is_valid_ghjaabcc(self):
        self.assertTrue(Day11.is_valid_password("ghjaabcc"))

    def test_next_after_abcdefgh(self):
        self.assertEqual("abcdffaa", Day11.next_password("abcdefgh"))

    def test_next_after_ghijklmn(self):
        self.assertEqual("ghjaabcc", Day11.next_password("ghijklmn"))

if __name__ == '__main__':
    unittest.main(verbosity=2)
