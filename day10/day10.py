interesting_cycles = [20, 60, 100, 140, 180, 220]


def parse_instr(str):
    if len(str) == 0:
        return None

    fields = str.split()
    if len(fields) == 1:
        return fields
    else:
        return [fields[0], int(fields[1])]


def apply_instr(x, instr):
    if instr[0] == 'noop':
        return [x]
    elif instr[0] == 'addx':
        return [x, x + instr[1]]


def calculate_signal_strength(results, interesting_cycles):
    # Calculate signal strength for each cycle
    # +1 because for cycle #i we're looking at the value for cycle #i-1
    signal_strength =  [(i+1+1) * k for i, k in enumerate(results)]

    # Filter interesting cycles
    return([signal_strength[cycle-1-1] for cycle in interesting_cycles])


def run_program(filename, verbose=False):
    with open(filename) as f:
        instructions = [parse_instr(line) for line in f]

    results = [1]
    if verbose:
        i = 1
    for instr in instructions:
        tmp = apply_instr(results[-1], instr)
        for elem in tmp:
            if verbose:
                print(i, elem, instr)
                i = i + 1
        results = results + tmp
    results = results[1:] # Remove first element (not an actual result)
    return results


if __name__ == "__main__":
    results = run_program('input.txt', verbose=True)
    print(sum(calculate_signal_strength(results, interesting_cycles)))