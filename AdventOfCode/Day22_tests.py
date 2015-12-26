import unittest

from Day22 import who_wins, spells

class Day22_tests(unittest.TestCase):
    def test_example_fight_1(self):
        player = {'hp': 10, 'mana': 250}
        boss = {'hp': 13, 'dmg': 8}
        self.assertEqual(who_wins(player, boss), "BossNoStrategy")

    def test_example_fight_2(self):
        player = {'hp': 10, 'mana': 250}
        boss = {'hp': 13, 'dmg': 8}
        strategy = [spells['Poison'], spells['Magic Missile']]
        self.assertEqual(who_wins(player, boss, strategy), "Player")

    def test_example_fight_3(self):
        player = {'hp': 10, 'mana': 250}
        boss = {'hp': 14, 'dmg': 8}
        strategy = [spells['Recharge'], spells['Shield'], spells['Drain'], spells['Poison'], spells['Magic Missile']]
        self.assertEqual(who_wins(player, boss, strategy), "Player")

if __name__ == "__main__":
    unittest.main(verbosity=2)
