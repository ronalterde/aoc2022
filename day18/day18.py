import sys
import numpy as np
from scipy.signal import convolve


def parse_input(filename):
    points = []
    with open(filename) as f:
        for line in f:
            line_list = line.strip().split(',')
            points.append([int(i) for i in line_list])

    x_max = max([i[0] for i in points])
    y_max = max([i[1] for i in points])
    z_max = max([i[2] for i in points])

    droplet = np.zeros((x_max + 1, y_max + 1, z_max + 1), dtype='int')

    for point in points:
        x = point[0]
        y = point[1]
        z = point[2]
        droplet[x][y][z] = 1

    return droplet


def make_filter_kernel():
    kernel = np.zeros((3, 3, 3), dtype='int')
    '''Create a kernel for summing up all neighbors

    Note we're not including the element itself.
    '''
    kernel[0, 1, 1] = 1
    kernel[2, 1, 1] = 1
    kernel[1, 0, 1] = 1
    kernel[1, 2, 1] = 1
    kernel[1, 1, 0] = 1
    kernel[1, 1, 2] = 1
    return kernel


def calculate_surface_area(droplet):
    '''Calculate total surface area

    1. Determine neighbor count for each cube
    2. Convert this to a 'surface count' (it's only a surface if the cube is not connected to another cube)
    3. Take relevant results only - cubes, not air
    4. Sum up total surface area
    '''
    kernel = make_filter_kernel()
    droplet_filtered_neighbor_count = convolve(droplet, kernel, mode='same')
    droplet_filtered_surface_count = 6 - droplet_filtered_neighbor_count
    droplet_filtered_surface_count_relevant = droplet_filtered_surface_count * droplet
    surface_area = np.sum(droplet_filtered_surface_count_relevant)
    return surface_area


def put_marker_on_reachable_air_fields(droplet):
    def in_range(p):
        return p[0] >= 0 and p[1] >= 0 and p[2] >= 0 and p[0] < droplet.shape[0] and p[1] < droplet.shape[1] and p[2] < droplet.shape[2]

    def put_marker(p):
        droplet[p] = 2 # Set marker so we can distinguish from '0' fields later.

        neighbor_candidates = [
                (p[0]-1, p[1], p[2]), # top
                (p[0]+1, p[1], p[2]), # bottom
                (p[0], p[1]-1, p[2]), # left
                (p[0], p[1]+1, p[2]), # right
                (p[0], p[1], p[2]+1),
                (p[0], p[1], p[2]-1),
                ]

        neighbors = [neighbor for neighbor in neighbor_candidates if in_range(neighbor) and droplet[neighbor] == 0]

        if len(neighbors) > 0:
            for neighbor in neighbors:
                put_marker(neighbor)
        else:
            return

    sys.setrecursionlimit(10000)

    put_marker((0, 0, 0))


def calculate_air_pocket_surface(droplet):
    '''Calculate surface of air pockets *not* reachable from outside droplet
    '''

    put_marker_on_reachable_air_fields(droplet)

    # Sum up fields that are still zero after putting markers
    kernel = make_filter_kernel()
    droplet_filtered_neighbor_count = convolve(droplet, kernel, mode='same')
    droplet_filtered_neighbor_count_relevant = droplet_filtered_neighbor_count * (droplet == 0)
    air_pocket_surface = np.sum(droplet_filtered_neighbor_count_relevant)
    return air_pocket_surface


if __name__ == "__main__":
    droplet = parse_input('input.txt')

    # Part 1
    surface_area = calculate_surface_area(droplet)
    print("Part 1:", surface_area)
    assert surface_area == 4456

    # Part 2
    air_pocket_surface = calculate_air_pocket_surface(droplet)
    assert air_pocket_surface == 1946
    print("Part 2:", surface_area - air_pocket_surface)
