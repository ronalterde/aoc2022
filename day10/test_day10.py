# Unittest support in VS Code: https://code.visualstudio.com/docs/python/testing

import unittest
from day10 import *


class TestPart1(unittest.TestCase):
    def test_parse_instr(self):
        self.assertEqual(parse_instr(''), None)
        self.assertEqual(parse_instr('noop'), ['noop'])
        self.assertEqual(parse_instr('addx 1'), ['addx', 1])
        self.assertEqual(parse_instr('addx -512'), ['addx', -512])

    def test_apply_instr(self):
        self.assertEqual(apply_instr(0, ['noop']), [0])

        self.assertEqual(apply_instr(0, ['addx', 0]), [0, 0])
        self.assertEqual(apply_instr(0, ['addx', 1]), [0, 1])
        self.assertEqual(apply_instr(1, ['addx', 1]), [1, 2])

    def test_calculate_signal_strength(self):
        self.assertEqual(sum(calculate_signal_strength([10, 20, 30, 40, 50], interesting_cycles=[2,4])),
            10 * 2 + 40 * 3)

    def test_example_data(self):
        results = run_program('example.txt')

        self.assertEqual(results[18], 21)
        self.assertEqual(results[58], 19)
        self.assertEqual(results[98], 18)
        self.assertEqual(results[138], 21)
        self.assertEqual(results[178], 16)
        self.assertEqual(results[218], 18)

        self.assertEqual(sum(calculate_signal_strength(results, interesting_cycles)), 13140)

    def test_real_data(self):
        results = run_program('input.txt')
        self.assertEqual(sum(calculate_signal_strength(results, interesting_cycles)), 13680)


class TestPart2(unittest.TestCase):
    def test_foo(self):
        pass
