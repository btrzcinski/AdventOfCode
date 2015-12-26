import unittest

import Day25

class Day25_tests(unittest.TestCase):
    def test_n_row_col_1_1(self):
        self.assertEqual(1, Day25.n_from_row_col(1, 1))

    def test_n_row_col_2_1(self):
        self.assertEqual(2, Day25.n_from_row_col(2, 1))

    def test_n_row_col_3_1(self):
        self.assertEqual(4, Day25.n_from_row_col(3, 1))

    def test_n_row_col_4_1(self):
        self.assertEqual(7, Day25.n_from_row_col(4, 1))

    def test_n_row_col_5_1(self):
        self.assertEqual(11, Day25.n_from_row_col(5, 1))

    def test_n_row_col_6_1(self):
        self.assertEqual(16, Day25.n_from_row_col(6, 1))

    def test_n_row_col_1_2(self):
        self.assertEqual(3, Day25.n_from_row_col(1, 2))

    def test_n_row_col_1_3(self):
        self.assertEqual(6, Day25.n_from_row_col(1, 3))

    def test_n_row_col_1_4(self):
        self.assertEqual(10, Day25.n_from_row_col(1, 4))

    def test_n_row_col_1_5(self):
        self.assertEqual(15, Day25.n_from_row_col(1, 5))

    def test_n_row_col_1_6(self):
        self.assertEqual(21, Day25.n_from_row_col(1, 6))

    def test_n_row_col_2_2(self):
        self.assertEqual(5, Day25.n_from_row_col(2, 2))

    def test_n_row_col_2_3(self):
        self.assertEqual(9, Day25.n_from_row_col(2, 3))

    def test_n_row_col_3_2(self):
        self.assertEqual(8, Day25.n_from_row_col(3, 2))

    def test_n_row_col_3_3(self):
        self.assertEqual(13, Day25.n_from_row_col(3, 3))

    def test_code_for_1(self):
        self.assertEqual(20151125, Day25.code_for_n(1))

    def test_code_for_2(self):
        self.assertEqual(31916031, Day25.code_for_n(2))

    def test_code_for_3(self):
        self.assertEqual(18749137, Day25.code_for_n(3))

    def test_code_for_1_1(self):
        self.assertEqual(20151125, Day25.code_for_row_col(1,1))

    def test_code_for_2_1(self):
        self.assertEqual(31916031, Day25.code_for_row_col(2,1))

    def test_code_for_1_2(self):
        self.assertEqual(18749137, Day25.code_for_row_col(1,2))

if __name__ == '__main__':
    unittest.main(verbosity=2)