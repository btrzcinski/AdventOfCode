import unittest

import Day17

class Day17_tests(unittest.TestCase):
    def test_example(self):
        containers = [20, 15, 10, 5, 5]
        actual_combinations = Day17.all_combinations_for_amount(containers, 25)
        expected_combinations = [(15, 10), (20, 5), (20, 5), (15, 5, 5)]
        self.assertCountEqual(expected_combinations, actual_combinations)

    def test_min_containers(self):
        containers = [20, 15, 10, 5, 5]
        all_combinations = Day17.all_combinations_for_amount(containers, 25)
        expected_minimum_combinations = [(15, 10), (20, 5), (20, 5)]
        actual_minimum_combinations = Day17.minimum_container_combinations(all_combinations)
        self.assertCountEqual(expected_minimum_combinations, actual_minimum_combinations)

if __name__ == '__main__':
    unittest.main(verbosity=2)
