import unittest

import Day5

class Day5_tests(unittest.TestCase):
    def test_part_1_case_1(self):
        self.assertTrue(Day5.part_1_is_nice_string("ugknbfddgicrmopn"))

    def test_part_1_case_2(self):
        self.assertTrue(Day5.part_1_is_nice_string("aaa"))

    def test_part_1_case_3(self):
        self.assertFalse(Day5.part_1_is_nice_string("jchzalrnumimnmhp"))

    def test_part_1_case_4(self):
        self.assertFalse(Day5.part_1_is_nice_string("haegwjzuvuyypxyu"))

    def test_part_1_case_5(self):
        self.assertFalse(Day5.part_1_is_nice_string("dvszwmarrgswjxmb"))

    def test_part_2_case_1(self):
        self.assertTrue(Day5.part_2_is_nice_string("qjhvhtzxzqqjkmpb"))

    def test_part_2_case_2(self):
        self.assertTrue(Day5.part_2_is_nice_string("xxyxx"))

    def test_part_2_case_3(self):
        self.assertFalse(Day5.part_2_is_nice_string("uurcxstgmygtbstg"))

    def test_part_2_case_4(self):
        self.assertFalse(Day5.part_2_is_nice_string("ieodomkazucvgmuy"))

if __name__ == '__main__':
    unittest.main(verbosity=2)
