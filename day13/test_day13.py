import unittest
from day13 import *

class TestDay13(unittest.TestCase):
    def test_rules(self):
        self.assertEqual(compare(0, 0), 0)
        self.assertEqual(compare(0, 1), -1)
        self.assertEqual(compare(1, 0), 1)

        self.assertEqual(compare([0], [0]), 0)
        self.assertEqual(compare([0], [1]), -1)
        self.assertEqual(compare([1], [0]), 1)
        self.assertEqual(compare([0], [0, 0]), -1)
        self.assertEqual(compare([0, 0], [0]), 1)
        self.assertEqual(compare([1,1,3,1,1], [1,1,5,1,1]), -1)

        self.assertEqual(compare([0], 0), 0)
        self.assertEqual(compare([0], 1), -1)
        self.assertEqual(compare([1], 0), 1)

    def test_example(self):
        self.assertEqual(compare([1,1,3,1,1], [1,1,5,1,1]), -1)
        self.assertEqual(compare([[1],[2,3,4]], [[1],4]), -1)
        self.assertEqual(compare([9], [[8,7,6]]), 1)
        self.assertEqual(compare([[4,4],4,4], [[4,4],4,4,4]), -1)
        self.assertEqual(compare([7,7,7,7], [7,7,7]), 1)
        self.assertEqual(compare([0], [3]), -1)
        self.assertEqual(compare([[[]]], [[]]), 1)
        self.assertEqual(compare([1,[2,[3,[4,[5,6,7]]]],8,9], [1,[2,[3,[4,[5,6,0]]]],8,9]), 1)

    def test_real(self):
        self.assertEqual(compare(7, [[6, 9, 0]]), 1)
        self.assertEqual(compare([[7,6],[],[[5],0,10,[7,9,[7],0]]], [[[[6,9,0]],0]]), 1)

    def test_parse_example(self):
        packets = parse_input('example.txt')
        self.assertEqual(len(packets), 8)

    def test_calculate_example(self):
        packets = parse_input('example.txt')
        self.assertEqual(calculate_sum_of_right(packets), 13)

    def test_calculate_real(self):
        packets = parse_input('input.txt')
        self.assertEqual(calculate_sum_of_right(packets), 6420)

    def test_encoder_key_example(self):
        packets = parse_input('example.txt')
        self.assertEqual(calculate_decoder_key(packets), 140)

    def test_encoder_key_real(self):
        packets = parse_input('input.txt')
        self.assertEqual(calculate_decoder_key(packets), 22000)
