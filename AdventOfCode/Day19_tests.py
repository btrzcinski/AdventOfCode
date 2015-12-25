import unittest

import Day19

class Day19_tests(unittest.TestCase):
    def test_example(self):
        replacement_map = {"H":["HO","OH"],"O":["HH"]}
        replacements = set(Day19.generated_molecules_from_molecule("HOH", replacement_map))
        self.assertCountEqual(["HOOH", "HOHO", "OHOH", "HHHH"], replacements)

    def test_example_part_2(self):
        replacement_map = {"e":["H","O"], "H":["HO","OH"], "O":["HH"]}
        steps = Day19.steps_to_get_molecule("HOH", replacement_map)
        self.assertEqual(3, steps)

if __name__ == "__main__":
    unittest.main(verbosity=2)
