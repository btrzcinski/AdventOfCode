import unittest

import Day21

class Day21_tests(unittest.TestCase):
    def test_example(self):
        player1 = {'hp': 8, 'dmg': 5, 'armor': 5}
        player2 = {'hp': 12, 'dmg': 7, 'armor': 2}
        self.assertEqual(1, Day21.who_wins(player1, player2))

if __name__ == "__main__":
    unittest.main(verbosity=2)
