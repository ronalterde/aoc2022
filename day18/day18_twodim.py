import numpy as np
from scipy.signal import convolve


def plot(mat):
    import matplotlib.pyplot as plt
    plt.rcParams["figure.figsize"] = [7.00, 3.50]
    plt.rcParams["figure.autolayout"] = True
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    z, x, y = mat.nonzero()
    ax.scatter(x, y, z, c=z, alpha=1)
    plt.show()


if __name__ == "__main__":
    ########################################
    # Part 1: Simple example in 2 dimensions
    a = np.array([[1, 1, 1], [1, 0, 1], [1, 0, 1], [0, 1, 0], [1, 1, 0]])
    kernel_2d = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
    sum_a = np.sum((4 - convolve(a, kernel_2d, mode='same')) * a)
    assert sum_a == 24
    print("sum_a:", sum_a)


    # ########################################
    # # Part 2: ignore air pockets not reachable from outside
    #
    # # Create padding around matrix so we can reach all '0' elements from there
    # # (might not be needed if we can assume starting at a '0' element)
    # a = np.concatenate((np.zeros((1, a.shape[1])), a, np.zeros((1, a.shape[1]))))
    # a = np.concatenate((np.zeros((a.shape[0], 1)), a, np.zeros((a.shape[0], 1))), axis=1)
    #
    # def in_range(p):
    #     return p[0] >= 0 and p[1] >= 0 and p[0] < a.shape[0] and p[1] < a.shape[1]
    #
    #
    # def f(p):
    #     a[p] = 2 # Set marker so we can distinguish from '0' fields later.
    #
    #     neighbors = [
    #             (p[0]-1, p[1]), # top
    #             (p[0]+1, p[1]), # bottom
    #             (p[0], p[1]-1), # left
    #             (p[0], p[1]+1), # right
    #             ]
    #
    #     n = [elem for elem in neighbors if in_range(elem) and a[elem] == 0]
    #
    #     if len(n) > 0:
    #         for elem in n:
    #             f(elem)
    #     else:
    #         return
    #
    # start = (0, 0)
    #
    # f(start)
    #
    # # Count edges between remaining '0' cubes and 1 cubes
    # aa = convolve(a, kernel_2d, mode='same')
    # aa = aa * (a == 0)
    # sum_c = np.sum(aa)
    # assert sum_c == 6
    # print(sum_c)
    # print("edges reachable from the outside:", sum_a - sum_c)
