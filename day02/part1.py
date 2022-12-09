"""
Score:
    A X Rock 1
    B Y Paper 2
    C Z Scissors 3

    Lose 0
    Win 6
    Draw 3

Rules:
    A X Draw 1+3
    A Y Win 2+6
    A Z Lose 3+0

    B X Lose 1+0
    B Y Draw 2+3
    B Z Win 3+6

    C X Win 1+6
    C Y Lose 2+0
    C Z Draw 3+3

Question: what would be your total score if you followed the strategy guide?
"""

def score(line):
    if line == "A X":
        return 1+3
    if line == "A Y":
        return 2+6
    if line == "A Z":
        return 3+0

    if line == "B X":
        return 1+0
    if line == "B Y":
        return 2+3
    if line == "B Z":
        return 3+6

    if line == "C X":
        return 1+6
    if line == "C Y":
        return 2+0
    if line == "C Z":
        return 3+3

with open('input.txt') as f:
    scores = []
    for line in f:
        scores.append(score(line.strip()))
    print(sum(scores))

