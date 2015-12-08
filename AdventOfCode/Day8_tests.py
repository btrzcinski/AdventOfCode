import unittest

import Day8

class Day8_tests(unittest.TestCase):
    def test_case_part_1_1(self):
        self.assertEqual("", Day8.input_string_to_pystr('""'))

    def test_case_part_1_2(self):
        self.assertEqual("abc", Day8.input_string_to_pystr('"abc"'))

    def test_case_part_1_3(self):
        self.assertEqual('aaa"aaa', Day8.input_string_to_pystr('"aaa\\"aaa"'))

    def test_case_part_1_4(self):
        self.assertEqual("'", Day8.input_string_to_pystr('"\\x27"'))

    def test_case_part_2_1(self):
        self.assertEqual(r'"\"\""', Day8.input_string_to_escaped_str('""'))

    def test_case_part_2_2(self):
        self.assertEqual(r'"\"abc\""', Day8.input_string_to_escaped_str('"abc"'))

    def test_case_part_2_3(self):
        self.assertEqual(r'"\"aaa\\\"aaa\""', Day8.input_string_to_escaped_str(r'"aaa\"aaa"'))

    def test_case_part_2_4(self):
        self.assertEqual(r'"\"\\x27\""', Day8.input_string_to_escaped_str(r'"\x27"'))

if __name__ == '__main__':
    unittest.main(verbosity=2)
