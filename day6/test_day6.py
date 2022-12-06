import unittest
from day6 import *


class TestPart1(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(find_marker('bvwbjplbgvbhsrlpgdmjqwftvncz'), 5)
        self.assertEqual(find_marker('nppdvjthqldpwncqszvftbrmjlhg'), 6)
        self.assertEqual(find_marker('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg'), 10)
        self.assertEqual(find_marker('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw'), 11)

    def test_input_file(self):
        with open('input.txt') as f:
            self.assertEqual(find_marker(f.read()), 1598)


class TestPart2(unittest.TestCase):
    def test_examples(self):
        self.assertEqual(find_marker('mjqjpqmgbljsphdztnvjfqwrcgsmlb', windowsize=14), 19)
        self.assertEqual(find_marker('bvwbjplbgvbhsrlpgdmjqwftvncz', windowsize=14), 23)
        self.assertEqual(find_marker('nppdvjthqldpwncqszvftbrmjlhg', windowsize=14), 23)
        self.assertEqual(find_marker('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg', windowsize=14), 29)
        self.assertEqual(find_marker('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw', windowsize=14), 26)

    def test_input_file(self):
        with open('input.txt') as f:
            self.assertEqual(find_marker(f.read(), windowsize=14), 2414)
