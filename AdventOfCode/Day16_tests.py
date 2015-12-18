import unittest

import Day16

class Day16_tests(unittest.TestCase):
	def test_part_one(self):
		aunt_map = Day16.get_aunt_map_from_file("Day16.txt")
		aunt_candidate = {
			'children': 3,
			'cats': 7,
			'samoyeds': 2,
			'pomeranians': 3,
			'akitas': 0,
			'vizslas': 0,
			'goldfish': 5,
			'trees': 3,
			'cars': 2,
			'perfumes': 1
		}
		best_match = Day16.best_match_for_candidate(aunt_map, aunt_candidate)
		self.assertEqual(213, best_match)
		
	def test_part_two(self):
		aunt_map = Day16.get_aunt_map_from_file("Day16.txt")
		aunt_candidate = {
			'children': 3,
			'cats': 7,
			'samoyeds': 2,
			'pomeranians': 3,
			'akitas': 0,
			'vizslas': 0,
			'goldfish': 5,
			'trees': 3,
			'cars': 2,
			'perfumes': 1
		}
		best_match = Day16.best_match_for_candidate(aunt_map, aunt_candidate, greater_keys=["cats", "trees"], lessthan_keys=["pomeranians", "goldfish"])
		self.assertEqual(323, best_match)

if __name__ == "__main__":
	unittest.main(verbosity=2)
