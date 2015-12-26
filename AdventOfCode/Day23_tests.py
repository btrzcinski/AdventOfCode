import unittest

from Day23 import run

class Day23_tests(unittest.TestCase):
    def test_example(self):
        program = [('inc', 'a'), ('jio', 'a', 2), ('tpl', 'a'), ('inc', 'a')]
        a, b = run(program)
        self.assertEqual(2, a)
        self.assertEqual(0, b)

if __name__ == "__main__":
    unittest.main(verbosity=2)
