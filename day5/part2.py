import re
from collections import deque
from part1 import split_stack_ids, split_into_bins, parse_procedure, push_row, read_file


if __name__ == "__main__":
    stacks, procedure_lines = read_file('input.txt')
    procedures = [parse_procedure(i) for i in procedure_lines]

    for procedure in procedures:
        temp = []
        for _ in range(procedure.count):
            temp.append(stacks[procedure.from_stack].pop())
        for item in reversed(temp):
            stacks[procedure.to_stack].append(item)

    # Print top stack elements
    print(''.join([stack.pop() for stack in stacks]))

    # The right answer is BPCZJLFJW
