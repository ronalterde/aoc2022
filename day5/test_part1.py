import unittest
from part1 import Procedure, split_stack_ids, split_into_bins, parse_procedure, push_row, read_file


def get_top_elements(stacks):
    return ''.join([stack[-1] for stack in stacks])


class TestIntegration(unittest.TestCase):
    def test_part1(self):
        stacks, procedure_lines = read_file('input.txt')
        procedures = [parse_procedure(i) for i in procedure_lines]

        for procedure in procedures:
            for _ in range(procedure.count):
                stacks[procedure.to_stack].append(stacks[procedure.from_stack].pop())

        self.assertEqual('QNHWJVJZW', get_top_elements(stacks))


    def test_part2(self):
        stacks, procedure_lines = read_file('input.txt')
        procedures = [parse_procedure(i) for i in procedure_lines]

        for procedure in procedures:
            temp = []
            for _ in range(procedure.count):
                temp.append(stacks[procedure.from_stack].pop())
            for item in reversed(temp):
                stacks[procedure.to_stack].append(item)

        self.assertEqual('BPCZJLFJW', get_top_elements(stacks))


class TestInputParsing(unittest.TestCase):
    def test_split_stack_ids(self):
        self.assertEqual([1, 2, 3], split_stack_ids('1 2 3'))
        self.assertEqual([41, 100, 345], split_stack_ids('41 100 345'))

    def test_split_into_bins(self):
        self.assertEqual([None], split_into_bins("", bin_count=1))
        self.assertEqual([None, None, None], split_into_bins("", bin_count=3))

        self.assertEqual(['A'], split_into_bins("[A]", bin_count=1))
        self.assertEqual(['A', 'B'], split_into_bins("[A] [B]", bin_count=2))
        self.assertEqual(['A', 'B', None], split_into_bins("[A] [B]    ", bin_count=3))

        self.assertEqual([None, 'B'], split_into_bins("    [B]", bin_count=2))
        self.assertEqual([None, None, 'C'], split_into_bins("        [C]", bin_count=3))

        self.assertEqual(['Z', 'Z', 'Q', 'S', 'F', 'P', 'B', 'Q', 'L'],
                split_into_bins('[Z] [Z] [Q] [S] [F] [P] [B] [Q] [L]', bin_count=9))

    def test_parse_procedure(self):
        self.assertEqual(Procedure(2, 0, 6), parse_procedure("move 2 from 1 to 7"))
        self.assertEqual(Procedure(100, 100, 101), parse_procedure("move 100 from 101 to 102"))


class TestStack(unittest.TestCase):
    def test_push_row(self):
        from collections import deque

        stacks = [deque() for _ in range(3)]

        push_row(stacks, [None, None, None])

        self.assertEqual(0, len(stacks[0]))
        self.assertEqual(0, len(stacks[1]))
        self.assertEqual(0, len(stacks[2]))


        stacks = [deque() for _ in range(3)]

        push_row(stacks, ['A', None, None])

        self.assertEqual(1, len(stacks[0]))
        self.assertEqual(0, len(stacks[1]))
        self.assertEqual(0, len(stacks[2]))


        stacks = [deque() for _ in range(3)]

        push_row(stacks, [None, 'A', None])
        push_row(stacks, [None, 'B', None])

        self.assertEqual(0, len(stacks[0]))
        self.assertEqual(2, len(stacks[1]))
        self.assertEqual(0, len(stacks[2]))

        self.assertEqual('B', stacks[1].pop())
        self.assertEqual('A', stacks[1].pop())
