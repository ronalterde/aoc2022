import numpy as np
from scipy.signal import convolve

def parse_input(filename):
    points = []
    with open(filename) as f:
        for line in f:
            line_list = line.strip().split(',')
            points.append([int(i) for i in line_list])
    return points


if __name__ == "__main__":
    # a) Simple example in 2 dimensions:
    a = np.array([[0, 0, 1], [0, 1, 0], [1, 1, 1], [0, 1, 0], [0, 0, 1]])
    kernel_2d = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
    sum_a = np.sum((4 - convolve(a, kernel_2d, mode='same')) * a)
    # print(sum_a)

    # b) The real thing in 3 dimensions:
    points = parse_input('input.txt')

    x_max = max([i[0] for i in points])
    y_max = max([i[1] for i in points])
    z_max = max([i[2] for i in points])

    mat = np.zeros((x_max + 1, y_max + 1, z_max + 1), dtype='int')

    for point in points:
        x = point[0]
        y = point[1]
        z = point[2]
        mat[x][y][z] = 1

    kernel_3d = np.zeros((3, 3, 3), dtype='int')
    kernel_3d[0, 1, 1] = 1
    kernel_3d[2, 1, 1] = 1
    kernel_3d[1, 0, 1] = 1
    kernel_3d[1, 2, 1] = 1
    kernel_3d[1, 1, 0] = 1
    kernel_3d[1, 1, 2] = 1

    sum_b = np.sum((6 - convolve(mat, kernel_3d, mode='same')) * mat)
    print("Part 1:", sum_b)

    # import matplotlib.pyplot as plt
    #
    # plt.rcParams["figure.figsize"] = [7.00, 3.50]
    # plt.rcParams["figure.autolayout"] = True
    # fig = plt.figure()
    # ax = fig.add_subplot(111, projection='3d')
    #
    # z, x, y = kernel.nonzero()
    # ax.scatter(x, y, z, c=z, alpha=1)
    #
    # plt.show()

    # c) Part 2: ignore inner cubes of air not reachable from outside.
    # Find '0' cubes fully framed by '1' cubes
    aa = convolve(a, kernel_2d, mode='same')
    aa = 4 * (aa == 4)
    aa = aa * (a == 0)
    sum_c = np.sum(aa)
    # print(sum)

    # d) Now do the same for 3d array:
    aa = convolve(mat, kernel_3d, mode='same')
    aa = 6 * (aa == 6)
    aa = aa * (mat == 0)
    sum_d = np.sum(aa)
    print("Part 2:", sum_b - sum_d)
