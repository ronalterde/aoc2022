import re
from collections import deque
from part1 import split_stack_ids, split_into_bins, parse_procedure, push_row


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

            temp = []
            for _ in range(count):
                temp.append(stacks[from_stack].pop())
            for item in reversed(temp):
                stacks[to_stack].append(item)

        # Print top stack elements
        print(''.join([stack.pop() for stack in stacks]))

        # The right answer is QNHWJVJZW
