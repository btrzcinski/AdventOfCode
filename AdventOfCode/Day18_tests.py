import unittest

import Day18

class Day18_tests(unittest.TestCase):
    def test_lightboard_neighbors(self):
        l = Day18.Lightboard(6)
        l[3,3] = 1
        for point in [(2,2), (2, 3), (2, 4), (3, 2), (3, 4), (4, 2), (4, 3), (4, 4)]:
            self.assertEqual(1, l.neighbors_on_for_light(point))

    def test_example(self):
        l = Day18.Lightboard(6)
        l[0,1] = 1
        l[0,3] = 1
        l[0,5] = 1
        l[1,3] = 1
        l[1,4] = 1
        l[2,0] = 1
        l[2,5] = 1
        l[3,2] = 1
        l[4,0] = 1
        l[4,2] = 1
        l[4,5] = 1
        l[5,0] = 1
        l[5,1] = 1
        l[5,2] = 1
        l[5,3] = 1
        self.assertEqual(".#.#.#\n...##.\n#....#\n..#...\n#.#..#\n####..", repr(l))
        l.iterate()
        self.assertEqual("..##..\n..##.#\n...##.\n......\n#.....\n#.##..", repr(l))
        l.iterate()
        self.assertEqual("..###.\n......\n..###.\n......\n.#....\n.#....", repr(l))
        l.iterate()
        self.assertEqual("...#..\n......\n...#..\n..##..\n......\n......", repr(l))
        l.iterate()
        self.assertEqual("......\n......\n..##..\n..##..\n......\n......", repr(l))

    def test_example_with_stuck_corners(self):
        l = Day18.Lightboard(6)
        l[0,0] = 1
        l[0,1] = 1
        l[0,3] = 1
        l[0,5] = 1
        l[1,3] = 1
        l[1,4] = 1
        l[2,0] = 1
        l[2,5] = 1
        l[3,2] = 1
        l[4,0] = 1
        l[4,2] = 1
        l[4,5] = 1
        l[5,0] = 1
        l[5,1] = 1
        l[5,2] = 1
        l[5,3] = 1
        l[5,5] = 1
        self.assertEqual("##.#.#\n...##.\n#....#\n..#...\n#.#..#\n####.#", repr(l))
        l.iterate(corners_always_on=True)
        self.assertEqual("#.##.#\n####.#\n...##.\n......\n#...#.\n#.####", repr(l))
        l.iterate(corners_always_on=True)
        self.assertEqual("#..#.#\n#....#\n.#.##.\n...##.\n.#..##\n##.###", repr(l))
        l.iterate(corners_always_on=True)
        self.assertEqual("#...##\n####.#\n..##.#\n......\n##....\n####.#", repr(l))
        l.iterate(corners_always_on=True)
        self.assertEqual("#.####\n#....#\n...#..\n.##...\n#.....\n#.#..#", repr(l))
        l.iterate(corners_always_on=True)
        self.assertEqual("##.###\n.##..#\n.##...\n.##...\n#.#...\n##...#", repr(l))
        self.assertEqual(17, l.number_of_lights_on())

    def test_example_with_stuck_corners_2(self):
        l = Day18.Lightboard(6)
        l[0,0] = 1
        l[0,1] = 1
        l[0,3] = 1
        l[0,5] = 1
        l[1,3] = 1
        l[1,4] = 1
        l[2,0] = 1
        l[2,5] = 1
        l[3,2] = 1
        l[4,0] = 1
        l[4,2] = 1
        l[4,5] = 1
        l[5,0] = 1
        l[5,1] = 1
        l[5,2] = 1
        l[5,3] = 1
        l[5,5] = 1
        self.assertEqual("##.#.#\n...##.\n#....#\n..#...\n#.#..#\n####.#", repr(l))
        l.iterate(n=5, corners_always_on=True)
        self.assertEqual("##.###\n.##..#\n.##...\n.##...\n#.#...\n##...#", repr(l))
        self.assertEqual(17, l.number_of_lights_on())

    def test_example_with_stuck_corners_3(self):
        l = Day18.Lightboard(6)
        l[0,1] = 1
        l[0,3] = 1
        l[0,5] = 1
        l[1,3] = 1
        l[1,4] = 1
        l[2,0] = 1
        l[2,5] = 1
        l[3,2] = 1
        l[4,0] = 1
        l[4,2] = 1
        l[4,5] = 1
        l[5,0] = 1
        l[5,1] = 1
        l[5,2] = 1
        l[5,3] = 1
        self.assertEqual(".#.#.#\n...##.\n#....#\n..#...\n#.#..#\n####..", repr(l))
        l.iterate(n=5, corners_always_on=True)
        self.assertEqual("##.###\n.##..#\n.##...\n.##...\n#.#...\n##...#", repr(l))
        self.assertEqual(17, l.number_of_lights_on())

if __name__ == "__main__":
    unittest.main(verbosity=2)
