"""
Update: second column says how the round needs to end - NOT what you need to choose.

X: you lose
Y: draw
Z: you win

-> need to find the shape to reach that outcome & calculate as before
"""

def deduce_my_shape(opponent_shape, outcome):
    # X: lose (0), Y: draw (3), Z: win (6)
    if opponent_shape == 'A' and outcome == 'X':
        return 'Z'
    if opponent_shape == 'A' and outcome == 'Y':
        return 'X'
    if opponent_shape == 'A' and outcome == 'Z':
        return 'Y'

    if opponent_shape == 'B' and outcome == 'X':
        return 'X'
    if opponent_shape == 'B' and outcome == 'Y':
        return 'Y'
    if opponent_shape == 'B' and outcome == 'Z':
        return 'Z'

    if opponent_shape == 'C' and outcome == 'X':
        return 'Y'
    if opponent_shape == 'C' and outcome == 'Y':
        return 'Z'
    if opponent_shape == 'C' and outcome == 'Z':
        return 'X'


def score(opponent_shape, my_shape):
    if opponent_shape == "A" and my_shape == "X":
        return 1+3
    if opponent_shape == "A" and my_shape == "Y":
        return 2+6
    if opponent_shape == "A" and my_shape == "Z":
        return 3+0

    if opponent_shape == "B" and my_shape == "X":
        return 1+0
    if opponent_shape == "B" and my_shape == "Y":
        return 2+3
    if opponent_shape == "B" and my_shape == "Z":
        return 3+6

    if opponent_shape == "C" and my_shape == "X":
        return 1+6
    if opponent_shape == "C" and my_shape == "Y":
        return 2+0
    if opponent_shape == "C" and my_shape == "Z":
        return 3+3


with open('input.txt') as f:
    scores = []
    for line in f:
        fields = line.strip().split(' ')
        opponent_shape = fields[0]
        outcome = fields[1]
        my_shape = deduce_my_shape(opponent_shape, outcome)
        print(my_shape)
        scores.append(score(opponent_shape, my_shape))
    print(sum(scores))
