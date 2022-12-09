import unittest
from day9 import *


class TestPart1(unittest.TestCase):
    def test_touching(self):
        # x direction
        self.assertEqual(touching((0,0), (0,0)), True)
        self.assertEqual(touching((1,0), (0,0)), True)
        self.assertEqual(touching((-1,0), (0,0)), True)
        self.assertEqual(touching((2,0), (0,0)), False)

        # y direction
        self.assertEqual(touching((0,0), (0,0)), True)
        self.assertEqual(touching((0,1), (0,0)), True)
        self.assertEqual(touching((0,-1), (0,0)), True)
        self.assertEqual(touching((0,2), (0,0)), False)

        # both
        self.assertEqual(touching((1,0), (0,1)), True)
        self.assertEqual(touching((0,1), (1,0)), True)
        self.assertEqual(touching((2,1), (1,0)), True)
        self.assertEqual(touching((0,1), (2,0)), False)
        self.assertEqual(touching((1,0), (0,2)), False)

    def test_one_step_movements(self):
        # Tail won't move because it's touching
        self.assertEqual(move((0,0), (0,0), 'r'), ((1,0), (0,0)))
        self.assertEqual(move((0,0), (0,0), 'l'), ((-1,0), (0,0)))
        self.assertEqual(move((0,0), (0,0), 'u'), ((0,1), (0,0)))
        self.assertEqual(move((0,0), (0,0), 'd'), ((0,-1), (0,0)))

        # The same for different starting positions (tail still won't move)
        self.assertEqual(move((1,0), (1,0), 'r'), ((2,0), (1,0)))
        self.assertEqual(move((1,0), (1,0), 'l'), ((0,0), (1,0)))
        self.assertEqual(move((1,0), (1,0), 'u'), ((1,1), (1,0)))
        self.assertEqual(move((1,0), (1,0), 'd'), ((1,-1), (1,0)))

        # Head moves away far enough for tail to follow
        # case 1: keeping the same direction
        self.assertEqual(move((1,0), (0,0), 'r'), ((2,0), (1,0)))
        self.assertEqual(move((-1,0), (0,0), 'l'), ((-2,0), (-1,0)))
        self.assertEqual(move((0,1), (0,0), 'u'), ((0,2), (0,1)))
        self.assertEqual(move((0,-1), (0,0), 'd'), ((0,-2), (0,-1)))

        # Head moves away far enough for tail to follow
        # case 2: diagonal catch-up

        # dont' catch up too early:
        self.assertEqual(move((2,0), (1,0), 'u'), ((2,1), (1,0)))

        self.assertEqual(move((1,1), (0,0), 'r'), ((2,1), (1,1)))
        self.assertEqual(move((-1,1), (0,0), 'l'), ((-2,1), (-1,1)))
        self.assertEqual(move((1,1), (0,0), 'u'), ((1,2), (1,1)))
        self.assertEqual(move((1,-1), (0,0), 'd'), ((1,-2), (1,-1)))



    def test_game_single_direction(self):
        game = Game()

        # need to track tail position for each individual movement => state => class instance
        self.assertEqual(game.head, (0,0))
        self.assertEqual(game.tail, (0,0))

        game.apply_motion('r', 3)
        self.assertEqual(game.head, (3,0))
        self.assertEqual(game.tail, (2,0))
        self.assertEqual(game.tails, [(0,0), (0,0), (1,0), (2,0)])

    def test_game_multi_direction(self):
        game = Game()

        game.apply_motion('r', 2)
        self.assertEqual(game.head, (2,0))
        self.assertEqual(game.tail, (1,0))
        self.assertEqual(game.tails, [(0,0), (0,0), (1,0)])

        game.apply_motion('u', 2)
        self.assertEqual(game.head, (2,2))
        self.assertEqual(game.tail, (2,1))
        self.assertEqual(game.tails, [(0,0), (0,0), (1,0), (1,0), (2,1)])

    def test_game_example_data(self):
        commands = []
        with open('example.txt') as f:
            for line in f:
                commands.append(line.strip().split())
        game = Game()
        for command in commands:
            game.apply_motion(command[0].lower(), int(command[1]))

        self.assertEqual(len(set(game.tails)), 13)

    def test_game_real_data(self):
        commands = []
        with open('input.txt') as f:
            for line in f:
                commands.append(line.strip().split())
        game = Game()
        for command in commands:
            game.apply_motion(command[0].lower(), int(command[1]))

        self.assertEqual(len(set(game.tails)), 6256)


class TestPart2(unittest.TestCase):
    def test_game2(self):
        commands = []
        with open('input.txt') as f:
            for line in f:
                commands.append(line.strip().split())
        game = Game2(length=10)

        for command in commands:
            game.apply_motion(command[0].lower(), int(command[1]))

        self.assertEqual(len(game.visited), 2665)