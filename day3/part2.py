"""
- Elves divided into groups of three
- All 3 share an item ("their badge")
- Need to pull out all badges
- Find the item shared by 3 elves
- input is sorted by groups
- sum over priorities for each group badge
"""

from part1 import prio

if __name__ == "__main__":
    with open('input.txt') as f:
        prios = []
        group = []
        i = 1

        for line in f:
            group.append(set(line.strip()))
            
            if i % 3 == 0:
                badge = list(group[0].intersection(group[1]).intersection(group[2]))[0]
                prios.append(prio(badge))
                group = []

            i = i + 1

        print(sum(prios))
