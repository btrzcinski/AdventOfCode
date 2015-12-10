import unittest

import Day9

class Day9_tests(unittest.TestCase):
    def test_case_1(self):
        test_graph = {}
        Day9.add_connection_to_graph(test_graph, 'London', 'Dublin', 464)
        Day9.add_connection_to_graph(test_graph, 'London', 'Belfast', 518)
        Day9.add_connection_to_graph(test_graph, 'Dublin', 'Belfast', 141)
        actual = Day9.route(test_graph)
        self.assertEqual(605, actual[1]);

    def test_case_2(self):
        test_graph = {}
        Day9.add_connection_to_graph(test_graph, 'London', 'Dublin', 464)
        Day9.add_connection_to_graph(test_graph, 'London', 'Belfast', 518)
        Day9.add_connection_to_graph(test_graph, 'Dublin', 'Belfast', 141)
        actual = Day9.route(test_graph, longest_path=True)
        self.assertEqual(982, actual[1]);

if __name__ == '__main__':
    unittest.main()
