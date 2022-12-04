"""
- split in half
- make set of both halves
- compare sets
- translate to prio value
"""

def prio(letter):
    if letter.islower():
        return ord(letter) - ord('a') + 1
    else:
        return ord(letter) - ord('A') + 1 + 26

prios = []

if __name__ == "__main__":
    with open('input.txt') as f:
        for line in f:
            s = line.strip()
            left = s[:len(s)//2]
            right = s[len(s)//2:]
            item = set(left).intersection(set(right))
            item = list(item)[0]
            prios.append(prio(item))
        print(sum(prios))
