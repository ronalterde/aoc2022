import unittest
from day11 import *

class TestDay11(unittest.TestCase):
    def test_parse_monkey_no(self):
        self.assertEqual(parse_monkey_no(''), None)
        self.assertEqual(parse_monkey_no('Monkey 0:\n'), 0)
        self.assertEqual(parse_monkey_no('Monkey 999:\n'), 999)

    def test_parse_starting_items(self):
        self.assertEqual(parse_starting_items(''), None)
        self.assertEqual(parse_starting_items('Starting items: 0'), [0])
        self.assertEqual(parse_starting_items('Starting items: 0, 1'), [0, 1])
        self.assertEqual(parse_starting_items('Starting items: 79, 98'), [79, 98])

    def test_parse_operation(self):
        self.assertEqual(parse_operation(''), None)
        self.assertEqual(parse_operation('Operation: foo'), None)
        self.assertEqual(parse_operation('Operation: new = old * 19'), 'old * 19')

    def test_parse_test(self):
        self.assertEqual(parse_test(''), None)
        self.assertEqual(parse_test('Test: foo'), None)
        self.assertEqual(parse_test('Test: divisible by 23'), 23)
        self.assertEqual(parse_test('Test: divisible by 999'), 999)

    def test_parse_condition_true(self):
        self.assertEqual(parse_condition_true(''), None)
        self.assertEqual(parse_condition_true('If true: throw to monkey 2'), 2)

    def test_parse_condition_false(self):
        self.assertEqual(parse_condition_false(''), None)
        self.assertEqual(parse_condition_false('If false: throw to monkey 2'), 2)