import unittest
from part1 import split_stack_ids, split_into_bins, parse_procedure, push_row


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
        self.assertEqual([2, 1, 7], parse_procedure("move 2 from 1 to 7"))
        self.assertEqual([100, 101, 102], parse_procedure("move 100 from 101 to 102"))

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
