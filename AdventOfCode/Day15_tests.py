import unittest

import Day15

class Day15_tests(unittest.TestCase):
    def test_example(self):
        props = [[-1, -2, 6, 3], [2, 3, -2, -1]]
        solution = Day15.solve_for_x_from_props(props)
        self.assertEqual([44, 56], solution)
        score = Day15.evaluate_x_with_props(solution, props)
        self.assertEqual(62842880, score)

    def test_calories_for_x_with_example(self):
        self.assertEqual(500, Day15.calories_for_x([40, 60], [8, 3]))

    def test_example_with_cal_penalty(self):
        props = [[-1, -2, 6, 3], [2, 3, -2, -1]]
        cals = [8, 3]
        solution = Day15.solve_for_x_with_cal_penalty(props, cals, 500)
        self.assertEqual([40, 60], solution)
        score = Day15.evaluate_x_with_props(solution, props)
        self.assertEqual(57600000, score)

    def test_solution_without_cals(self):
        props = [[2,0,-2,0],[0,5,-3,0],[0,0,5,-1],[0,-1,0,5]]
        solution = Day15.solve_for_x_from_props(props)
        self.assertEqual([17, 19, 38, 26], solution)
        score = Day15.evaluate_x_with_props(solution, props)
        self.assertEqual(21367368, score)

    def test_solution_with_cals(self):
        props = [[2,0,-2,0],[0,5,-3,0],[0,0,5,-1],[0,-1,0,5]]
        cals = [3, 3, 8, 8]
        solution = Day15.solve_for_x_with_cal_penalty(props, cals, 500)
        self.assertEqual([46, 14, 30, 10], solution)
        score = Day15.evaluate_x_with_props(solution, props)
        self.assertEqual(1766400, score)
        cal_score = Day15.calories_for_x(solution, cals)
        self.assertEqual(500, cal_score)

if __name__ == '__main__':
    unittest.main(verbosity=2)
