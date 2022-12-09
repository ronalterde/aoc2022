class Game:
    def __init__(self):
        self.head = (0,0)
        self.tail = (0,0)
        self.tails = [(0,0)]

    def apply_motion(self, direction, count):
        for _ in range(count):
            self.head, self.tail = move(self.head, self.tail, direction)
            self.tails.append(self.tail)


def touching(head, tail):
    return abs(head[0]-tail[0]) <= 1 and abs(head[1]-tail[1]) <= 1


def move(head, tail, direction):
    def transform(point, direction):
        if direction == 'r':
            return (point[0]+1, point[1])
        elif direction == 'l':
            return (point[0]-1, point[1])
        elif direction == 'u':
            return (point[0], point[1]+1)
        elif direction == 'd':
            return (point[0], point[1]-1)
        else:
            return None

    new_head = transform(head, direction)
    new_tail = tail

    if not touching(new_head, new_tail):
        new_tail = transform(new_tail, direction)
        if direction == 'r':
            new_tail = (new_tail[0], new_head[1])
        elif direction == 'l':
            new_tail = (new_tail[0], new_head[1])
        elif direction == 'u':
            new_tail = (new_head[0], new_tail[1])
        elif direction == 'd':
            new_tail = (new_head[0], new_tail[1])
        else:
            pass
    return new_head, new_tail


def move_multiple(knots, direction):
    def transform(point, direction):
        if direction == 'r':
            return (point[0]+1, point[1])
        elif direction == 'l':
            return (point[0]-1, point[1])
        elif direction == 'u':
            return (point[0], point[1]+1)
        elif direction == 'd':
            return (point[0], point[1]-1)
        else:
            return None

    knots[0] = transform(knots[0], direction)

    for i, _ in enumerate(knots[:-1]):
        h = knots[i]
        t = knots[i+1]

        x_diff = h[0] - t[0]
        y_diff = h[1] - t[1]

        if abs(x_diff) <= 1 and abs(y_diff) <= 1:
            # touching => nothing to do
            pass
        elif abs(x_diff) == 2 and abs(y_diff) == 0:
            # move horiz. without diagonal offset
            t = (t[0] + x_diff/2, t[1])
        elif abs(x_diff) == 0 and abs(y_diff) == 2:
            # move vertic. without diagonal offset
            t = (t[0], t[1] + y_diff/2)
        elif abs(x_diff) == 2 and abs(y_diff) == 1:
            # move horiz. with diagonal offset
            t = (t[0] + x_diff/2, t[1] + y_diff)
        elif abs(x_diff) == 1 and abs(y_diff) == 2:
            # move vertic. with diagonal offset
            t = (t[0] + x_diff, t[1] + y_diff/2)
        elif abs(x_diff) == 2 and abs(y_diff) == 2:
            # move diagonally
            t = (t[0] + x_diff/2, t[1] + y_diff/2)
        else:
            pass

        knots[i+1] = t

    return knots


def print_rope(knots):
    names = ['H'] + list(range(1, len(knots)))
    for i in reversed(range(5)):
        for k in range(6):
            item = (k, i)
            if item in knots:
                idx = list(knots).index(item)
                name = list(names)[idx]
                print(name, end='')
            else:
                print('.', end='')
        print('')


class Game2:
    def __init__(self, length):
        self.knots = [(0,0)] * length
        self.visited = set()

    def apply_motion(self, direction, count):
        for _ in range(count):
            self.knots = move_multiple(self.knots, direction)
            self.visited.add(self.knots[-1])


if __name__ == "__main__":
    commands = []
    # with open('input.txt') as f:
    with open('example.txt') as f:
        for line in f:
            commands.append(line.strip().split())
    game = Game2(length=10)
    print_rope(game.knots)
    print()

    for command in commands:
        print(command)
        game.apply_motion(command[0].lower(), int(command[1]))
        print_rope(game.knots)
        print()

    print(len(game.visited))