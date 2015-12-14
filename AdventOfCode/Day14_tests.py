import unittest

import Day14

class Day14_tests(unittest.TestCase):
    def setUp(self):
        self.comet = Day14.Reindeer(name="Comet", speed=14, flying_time=10, resting_time=127)
        self.dancer = Day14.Reindeer(name="Dancer", speed=16, flying_time=11, resting_time=162)

    def test_one_second(self):
        self.assertEqual(14, self.comet.distance_traveled_by_time(1))
        self.assertEqual(16, self.dancer.distance_traveled_by_time(1))

    def test_eleven_seconds(self):
        self.assertEqual(140, self.comet.distance_traveled_by_time(11))
        self.assertEqual(176, self.dancer.distance_traveled_by_time(11))

    def test_thousand_seconds(self):
        self.assertEqual(1120, self.comet.distance_traveled_by_time(1000))
        self.assertEqual(1056, self.dancer.distance_traveled_by_time(1000))

if __name__ == '__main__':
    unittest.main(verbosity=2)
