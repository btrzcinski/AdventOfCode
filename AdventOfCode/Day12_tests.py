import unittest

from Day12 import sum_of_numbers_in_json as sut

class Day12_tests(unittest.TestCase):
    def test_case_1(self):
        doc1 = """[1,2,3]"""
        doc2 = """{"a":2,"b":4}"""
        self.assertEqual(6, sut(doc1))
        self.assertEqual(6, sut(doc2))

    def test_case_2(self):
        doc1 = """[[[3]]]"""
        doc2 = """{"a":{"b":4},"c":-1}"""
        self.assertEqual(3, sut(doc1))
        self.assertEqual(3, sut(doc2))

    def test_case_3(self):
        doc1 = """{"a":[-1,1]}"""
        doc2 = """[-1,{"a":1}]"""
        self.assertEqual(0, sut(doc1))
        self.assertEqual(0, sut(doc2))

    def test_case_4(self):
        doc1 = """[]"""
        doc2 = """{}"""
        self.assertEqual(0, sut(doc1))
        self.assertEqual(0, sut(doc2))

    def test_case_nored_1(self):
        doc = """[1,2,3]"""
        self.assertEqual(6, sut(doc, True))

    def test_case_nored_2(self):
        doc = """[1,{"c":"red","b":2},3]"""
        self.assertEqual(4, sut(doc, True))

    def test_case_nored_3(self):
        doc = """{"d":"red","e":[1,2,3,4],"f":5}"""
        self.assertEqual(0, sut(doc, True))

    def test_case_nored_4(self):
        doc = """[1,"red",5]"""
        self.assertEqual(6, sut(doc, True))

    def test_case_nored_5(self):
        doc = """{"a":2,"3":"b","c":[1, "red", 2]}"""
        self.assertEqual(5, sut(doc, True))

if __name__ == '__main__':
    unittest.main(verbosity=2)
