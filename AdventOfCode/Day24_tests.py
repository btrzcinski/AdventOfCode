import unittest

import Day24

class Day24_tests(unittest.TestCase):
    def test_example(self):
        pl = [1,3,4,5,7,2,8,10,11,9]
        best_groups = list(Day24.valid_groups(pl, 2))
        a_best_group = best_groups[0]
        self.assertEqual(sum(a_best_group[0]), sum(a_best_group[1]))
        self.assertEqual(sum(a_best_group[0]), sum(a_best_group[2]))
        self.assertEqual(sum(a_best_group[0]), 20)

    def test_best_qe_example(self):
        pl = [1,3,4,5,7,2,8,10,11,9]
        best_qe = Day24.best_qe(pl)
        self.assertEqual(99, best_qe[0])

    def test_best_qe_example_4(self):
        pl = [1,3,4,5,7,2,8,10,11,9]
        best_qe = Day24.best_qe(pl, 4)
        self.assertEqual(44, best_qe[0])

if __name__ == '__main__':
    unittest.main(verbosity=2)