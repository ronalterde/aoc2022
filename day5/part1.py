"""
- Read initial configuaration of each stack
- Apply procedure, one at a time
- Print top stack elements

Example:
[D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
"""

import re
from collections import deque


def split_stack_ids(line):
    return [int(i) for i in line.strip().split()]


def split_into_bins(input_string, bin_count):
    bins = [None] * bin_count
    state = 'expect_open'
    current_bin = 0
    space_count = 0

    for char in input_string:
        if state == 'expect_open':
            if char == '[':
                state = 'expect_item'
                space_count = 0
            elif char == ' ':
                space_count = space_count + 1
        elif state == 'expect_item':
            bins[current_bin] = char
            state = 'expect_close'
        elif state == 'expect_close':
            if char == ']':
                current_bin = current_bin + 1
                state = 'expect_open'

        # Skip empty bin: leave at None
        if space_count == 4:
            current_bin = current_bin + 1
            space_count = 0
    return bins


def parse_procedure(s):
    pattern = re.compile("move (\d*) from (\d*) to (\d*)")
    match_groups = pattern.fullmatch(s).groups()
    return [int(i) for i in match_groups]


def push_row(stacks, row):
   for i in range(len(stacks)):
       if row[i] != None:
           stacks[i].append(row[i])


if __name__ == "__main__":
    with open('input.txt') as f:
        l = f.readlines()

        header_lines = []
        body_lines = []

        got_empty_line = False
        for line in l:
            if line.strip() == '':
                got_empty_line = True
                continue

            if not got_empty_line:
                header_lines.append(line.strip())
            else:
                body_lines.append(line.strip())

        stack_ids = [int(i) for i in header_lines[-1].split()]
        stack_count = len(stack_ids)
        header_lines = header_lines[:-1]

        stacks = [deque() for _ in range(stack_count)]

        for line in reversed(header_lines):
            bins = split_into_bins(line, bin_count=stack_count)
            push_row(stacks, bins)

        # Apply procedures
        for line in body_lines:
            procedure = parse_procedure(line.strip())
            count = procedure[0]
            from_stack = procedure[1] - 1
            to_stack = procedure[2] - 1

            for _ in range(count):
                stacks[to_stack].append(stacks[from_stack].pop())

        # Print top stack elements
        print(''.join([stack.pop() for stack in stacks]))

        # The right answer is QNHWJVJZW
