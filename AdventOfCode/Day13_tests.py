import unittest

import Day13

class Day13_tests(unittest.TestCase):
    def test_example(self):
        sc = Day13.SeatingCalculator()
        sc.set_happiness_value("Alice", "Bob", 54)
        sc.set_happiness_value("Alice", "Carol", -79)
        sc.set_happiness_value("Alice", "David", -2)
        sc.set_happiness_value("Bob", "Alice", 83)
        sc.set_happiness_value("Bob", "Carol", -7)
        sc.set_happiness_value("Bob", "David", -63)
        sc.set_happiness_value("Carol", "Alice", -62)
        sc.set_happiness_value("Carol", "Bob", 60)
        sc.set_happiness_value("Carol", "David", 55)
        sc.set_happiness_value("David", "Alice", 46)
        sc.set_happiness_value("David", "Bob", -7)
        sc.set_happiness_value("David", "Carol", 41)
        self.assertEqual(330, sc.most_optimal_arrangement()[0])

if __name__ == '__main__':
    unittest.main(verbosity=2)
