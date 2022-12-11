import re
import math
import numpy as np


PART1 = False
if PART1:
    ROUNDS = 20
else:
    ROUNDS = 10000


def parse_monkey_no(line):
    match = re.search("Monkey ([0-9]*):", line)
    if match:
        return int(match.group(1))
    else:
        return None


def parse_starting_items(line):
    match = re.search("Starting items: (.*)", line)
    if match:
        fields = match.group(1).split(',')
        return [int(i) for i in fields]


def parse_operation(line):
    match = re.search("Operation: new = (.*)", line)
    if match:
        return match.group(1).strip()


def parse_test(line):
    match = re.search("Test:(.*)", line)
    if match:
        text = match.group(1).strip()
        match = re.search("divisible by ([0-9]*)", text)
        if match:
            return int(match.group(1))


def parse_condition_true(line):
    match = re.search("If true: throw to monkey ([0-9]*)", line)
    if match:
        return int(match.group(1).strip())


def parse_condition_false(line):
    match = re.search("If false: throw to monkey ([0-9]*)", line)
    if match:
        return int(match.group(1).strip())


def complete(monkey):
    return 'starting_items' in monkey and 'operation' in monkey\
        and 'divisor' in monkey and 'condition_true' in monkey and 'condition_false' in monkey


def parse_input_file(filename):
    monkeys = {}
    current_monkey_no = None

    with open(filename) as f:
        state = 'wait_for_monkey'
        for line in f:
            if state == 'wait_for_monkey':
                no = parse_monkey_no(line)
                if no != None:
                    assert not no in monkeys
                    current_monkey_no = no
                    monkeys[current_monkey_no] = { }
                    state = 'process_data'
            elif state == 'process_data':
                starting_items = parse_starting_items(line)
                if starting_items:
                    monkeys[current_monkey_no]['starting_items'] = starting_items

                operation = parse_operation(line)
                if operation != None:
                    monkeys[current_monkey_no]['operation'] = operation

                divisor = parse_test(line)
                if divisor != None:
                    monkeys[current_monkey_no]['divisor'] = divisor

                condition_true = parse_condition_true(line)
                if condition_true != None:
                    monkeys[current_monkey_no]['condition_true'] = condition_true

                condition_false = parse_condition_false(line)
                if condition_false != None:
                    monkeys[current_monkey_no]['condition_false'] = condition_false

                if complete(monkeys[current_monkey_no]):
                    monkeys[current_monkey_no]['inspected_count'] = 0
                    state = 'wait_for_monkey'

        return monkeys    


if __name__ == "__main__":
    monkeys = parse_input_file('input.txt')

    # Idea from: https://github.com/xconnected/adventofcode/blob/main/2022/day11.py
    common_divisor = np.lcm.reduce([monkeys[i]['divisor'] for i in monkeys])

    for round in range(ROUNDS):
        for i in monkeys:
            items = monkeys[i]['starting_items']
            monkeys[i]['inspected_count'] = monkeys[i]['inspected_count'] + len(items)
            if len(items) > 0:
                for value in items:
                    value = value % common_divisor
                    old = value
                    value = eval(monkeys[i]['operation'])
                    if PART1:
                        value = int(value / 3)
                    divisor = monkeys[i]['divisor']
                    test_result = value % divisor == 0
                    if test_result:
                        dest_monkey = monkeys[i]['condition_true']
                    else:
                        dest_monkey = monkeys[i]['condition_false']
                    monkeys[dest_monkey]['starting_items'].append(value)
                monkeys[i]['starting_items'].clear()

    print('monkey business:', math.prod(sorted([monkeys[i]['inspected_count'] for i in monkeys])[-2:]))
