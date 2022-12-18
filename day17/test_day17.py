import unittest
import numpy.testing
import numpy as np
from day17 import *


class TestDay17(unittest.TestCase):
    def test_make_rock(self):
        numpy.testing.assert_allclose(make_rock([(0, 0), (1, 0), (2, 0), (3, 0)]),
                np.array([[0, 0, 1, 1, 1, 1, 0]]))

        numpy.testing.assert_allclose(make_rock([(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)]),
                np.array([
                    [0, 0, 0, 1, 0, 0, 0],
                    [0, 0, 1, 1, 1, 0, 0],
                    [0, 0, 0, 1, 0, 0, 0]]))

    def test_push(self):
        numpy.testing.assert_allclose(push(np.array([[0, 0, 0]]), '>'), np.array([[0, 0, 0]]))
        numpy.testing.assert_allclose(push(np.array([[0, 1, 0]]), '>'), np.array([[0, 0, 1]]))
        numpy.testing.assert_allclose(push(np.array([[0, 0, 1]]), '>'), np.array([[0, 0, 1]]))
        numpy.testing.assert_allclose(push(np.array([[0, 1, 0], [0, 1, 0]]), '>'), np.array([[0, 0, 1], [0, 0, 1]]))

        numpy.testing.assert_allclose(push(np.array([[0, 0, 0]]), '<'), np.array([[0, 0, 0]]))
        numpy.testing.assert_allclose(push(np.array([[0, 1, 0]]), '<'), np.array([[1, 0, 0]]))
        numpy.testing.assert_allclose(push(np.array([[1, 0, 0]]), '<'), np.array([[1, 0, 0]]))
        numpy.testing.assert_allclose(push(np.array([[0, 1, 0], [0, 1, 0]]), '<'), np.array([[1, 0, 0], [1, 0, 0]]))

    def test_check_collision(self):
        self.assertFalse(check_collision(tower=np.array([[0, 0, 0]]), rock=np.array([[0, 0, 0]]), overlap=1))
        self.assertFalse(check_collision(tower=np.array([[1, 0, 1]]), rock=np.array([[0, 1, 0]]), overlap=1))

        self.assertFalse(check_collision(tower=np.array([[0, 1, 0]]), rock=np.array([[0, 1, 0], [0, 0, 0]]), overlap=1))

        self.assertTrue(check_collision(tower=np.array([[0, 0, 0], [0, 1, 0]]), rock=np.array([[0, 0, 0], [0, 1, 0]]), overlap=2))

        rock = np.array([
            [0, 0, 0],
            [0, 0, 0],
            [0, 1, 0],
            ])

        tower = np.array([
            [0, 1, 0],
            [0, 0, 0],
            [0, 0, 0],
            ])

        self.assertTrue(check_collision(tower, rock, overlap=1))
        self.assertFalse(check_collision(tower, rock, overlap=2))
        self.assertFalse(check_collision(tower, rock, overlap=3))
        self.assertFalse(check_collision(tower, rock, overlap=0))


    def test_combine(self):
        rock = np.array([
            [0, 0, 0],
            [0, 0, 0],
            [0, 1, 0],
            ])

        tower = np.array([
            [0, 1, 0],
            [0, 0, 0],
            [0, 0, 0],
            ])

        numpy.testing.assert_allclose(combine(tower, rock, overlap=1), np.array([
            [0, 0, 0],
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0],
            [0, 0, 0]
            ]))

        numpy.testing.assert_allclose(combine(tower, rock, overlap=0), np.array([
            [0, 0, 0],
            [0, 0, 0],
            [0, 1, 0],
            [0, 1, 0],
            [0, 0, 0],
            [0, 0, 0]
            ]))

        numpy.testing.assert_allclose(combine(tower, rock, overlap=3), np.array([
            [0, 1, 0],
            [0, 0, 0],
            [0, 1, 0]
            ]))


        rock = np.array([
            [1, 1, 0],
            [1, 1, 0],
            ])

        tower = np.array([
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
            ])

        numpy.testing.assert_allclose(combine(tower, rock, overlap=3), np.array([
            [0, 0, 0],
            [1, 1, 0],
            [1, 1, 0]
            ]))


if __name__ == "__main__":
    unittest.main()
