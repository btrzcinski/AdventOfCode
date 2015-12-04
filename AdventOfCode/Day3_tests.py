import unittest
import Day3

class TestDay3(unittest.TestCase):
	def test1_norobo(self):
		testdata = '>'
		self.assertEqual(Day3.total_delivered_houses(testdata, robosanta=False), 2)

	def test2_norobo(self):
		testdata = '^>v<'
		self.assertEqual(Day3.total_delivered_houses(testdata, robosanta=False), 4)

	def test3_norobo(self):
		testdata = '^v^v^v^v^v'
		self.assertEqual(Day3.total_delivered_houses(testdata, robosanta=False), 2)

	def test1_robo(self):
		testdata = '>'
		self.assertEqual(Day3.total_delivered_houses(testdata, robosanta=True), 2)

	def test2_robo(self):
		testdata = '^>v<'
		self.assertEqual(Day3.total_delivered_houses(testdata, robosanta=True), 3)

	def test3_robo(self):
		testdata = '^v^v^v^v^v'
		self.assertEqual(Day3.total_delivered_houses(testdata, robosanta=True), 11)

if __name__ == '__main__':
	unittest.main(verbosity=2)