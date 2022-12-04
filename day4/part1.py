"""
- each section has a unique ID number
- each elf is assigned a range of IDs
- some assignments overlap
- elves get together in pairs and compare their ranges

Question: find pairs where one fully contains the other.
"""

def split(line):
    fields = line.split(',')

    first = fields[0].split('-')
    first_start = first[0]
    first_end = first[1]

    second = fields[1].split('-')
    second_start = second[0]
    second_end = second[1]

    return ((int(first_start), int(first_end)), (int(second_start), int(second_end)))


def fully_contained(first, second):
    return first[0] >= second[0] and first[1] <= second[1]

if __name__ == "__main__":

    count = 0;
    with open('input.txt') as f:
        for line in f:
            fields = split(line.strip())
            if fully_contained(fields[0], fields[1]) or fully_contained(fields[1], fields[0]):
                count = count + 1
        print(count)
