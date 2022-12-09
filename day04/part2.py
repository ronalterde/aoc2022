"""
now look for intervals that overlap *at all*, not necessarily completely.
"""

from part1 import split

def contained(first, second):
    a = first[0]
    b = first[1]
    c = second[0]
    d = second[1]

    return (a <= c <= b) or (c <= a <= d)

if __name__ == "__main__":

    count = 0;
    with open('input.txt') as f:
        for line in f:
            fields = split(line.strip())
            if contained(fields[0], fields[1]) or contained(fields[1], fields[0]):
                count = count + 1
        print(count)
