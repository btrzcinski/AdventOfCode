import unittest

import Day6

class Day6_tests(unittest.TestCase):
    def test_turn_on(self):
        lights = Day6.all_lights_off()
        Day6.turn_on_lights(lights, (0, 0), (2, 2))
        for x in range(0,3):
            for y in range(0,3):
                self.assertTrue(lights[x][y])
        self.assertEqual(9, Day6.lit_lights(lights))

if __name__ == '__main__':
    unittest.main()
