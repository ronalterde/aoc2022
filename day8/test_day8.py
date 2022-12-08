import unittest
import numpy as np
from day8 import *


class TestPart1(unittest.TestCase):
    def test_example_from_left(self):
        trees = read_data('example.txt')
        left = for_all_rows(trees)

        expected = np.array([[0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0]])

        self.assertTrue(np.array_equal(left, expected))

    def test_example_from_right(self):
        trees = read_data('example.txt')
        trees_from_right = np.fliplr(trees)
        right = np.fliplr(for_all_rows(trees_from_right))

        expected = np.array([[0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]])

        self.assertTrue(np.array_equal(right, expected))

    def test_example_from_top(self):
        trees = read_data('example.txt')
        trees_from_top = np.transpose(trees)
        top = np.transpose(for_all_rows(trees_from_top))

        expected = np.array([[0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]])

        self.assertTrue(np.array_equal(top, expected))

    def test_example_from_bottom(self):
        trees = read_data('example.txt')
        trees_from_bottom = np.fliplr(np.transpose(trees))
        bottom = np.flipud(np.transpose(for_all_rows(trees_from_bottom)))

        expected = np.array([[0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0]])

        print(bottom)
        self.assertTrue(np.array_equal(bottom, expected))

    def test_all_directions_combined(self):
        trees = read_data('example.txt')
        combined = calculate_combined_map(trees)

        expected = np.array([[0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0]])

        self.assertTrue(np.array_equal(combined, expected))
        self.assertEqual(np.count_nonzero(combined), 5)

    def test_fill_outer_edges_and_count(self):
        trees = read_data('example.txt')
        combined = calculate_combined_map(trees)

        fill_outer_edges(combined)

        self.assertEqual(np.count_nonzero(combined), 21)

    def test_real_data(self):
        trees = read_data('input.txt')
        combined = calculate_combined_map(trees)

        fill_outer_edges(combined)

        self.assertEqual(np.count_nonzero(combined), 1825)

class TestPart2(unittest.TestCase):
    pass
