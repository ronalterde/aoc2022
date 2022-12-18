import numpy as np
from collections import deque

rock_coords = [
        [(0, 0), (1, 0), (2, 0), (3, 0)],
        [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
        [(2, 0), (2, 1), (0, 2), (1, 2), (2, 2)],
        [(0, 0), (0, 1), (0, 2), (0, 3)],
        [(0, 0), (1, 0), (0, 1), (1, 1)]
        ]


def make_rock(coords):
    # Make initial state of rock, with correct right-shift:
    height = max([r[1] for r in coords]) + 1
    mat = np.zeros((7, height))

    for i in coords:
        mat[i] = 1
    mat = mat.transpose()
    mat = np.roll(mat, 2)
    return mat


jet = deque(">>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>")


def get_jet():
    value = jet[0]
    jet.rotate(-1)
    return value


def push(rock, jet):
    if jet == '>':
        # if last column is all zeros => no collision yet
        if sum(rock[:,-1]) == 0:
            rock = np.roll(rock, 1)
    elif jet == '<':
        # if first column is all zeros => no collision yet
        if sum(rock[:,0]) == 0:
            rock = np.roll(rock, -1)
    return rock


def check_collision(tower, rock, overlap=1):
    if overlap == 0:
        return False
    bottom_rock_rows = rock[-overlap:,:]
    top_tower_rows = tower[overlap-1,:]
    return np.any(np.logical_and(bottom_rock_rows, top_tower_rows))


def combine(tower, rock, overlap):
    if overlap == 0:
        return np.concatenate((rock, tower))
    overlap = min(overlap, rock.shape[0])
    top_rock_rows = rock[:rock.shape[0]-overlap]
    overlapping_rock_rows = rock[-overlap:]
    overlapping_tower_rows = tower[:overlap]
    overlap_area = np.logical_or(overlapping_rock_rows, overlapping_tower_rows)
    bottom_tower_rows = tower[overlap:]

    return np.concatenate((top_rock_rows, overlap_area, bottom_tower_rows))


def simulate_rock(tower, rock):
    # 3x push (these cannot collide)
    rock = push(rock, get_jet())
    rock = push(rock, get_jet())
    rock = push(rock, get_jet())

    # one last push before starting to overlap with existing tower
    rock = push(rock, get_jet())

    if not isinstance(tower, np.ndarray):
        return rock

    for overlap in range(tower.shape[0]):
        if not check_collision(tower, rock, overlap=overlap+1):
            jet = get_jet()
            test_rock = push(rock, jet)
            if not check_collision(tower, test_rock, overlap=overlap+1):
                rock = push(rock, jet)
        else:
            break

    tower = combine(tower, rock, overlap=overlap)
    return tower


if __name__ == "__main__":
    def simulate():
        rocks = [make_rock(i) for i in rock_coords]
        tower = None
        i = 0
        while True:
            for rock in rocks:
                tower = simulate_rock(tower, rock)
                if i > 2022:
                    print(tower.shape[0])
                    return
                i = i + 1

    simulate()

