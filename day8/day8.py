import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm


def read_data(filename):
    col_count = 0
    row_count = 0
    list_of_lists = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            row_count = row_count + 1
            col_count = len(line)
            int_list = [int(i) for i in list(line)]
            list_of_lists.append(int_list)

    return np.array(list_of_lists)


def find_visible_trees(in_mat):
    result = np.zeros_like(in_mat)
    for row_index, row in enumerate(in_mat[1:-1, :]):
        for i in range(1, len(row)-1):
            if row[i] > max(row[:i]):
                result[row_index+1, i] = 1
    return result


def calculate_viewing_distance(in_mat):
    result = np.zeros_like(in_mat)
    inner = in_mat[1:-1, :]
    for row_index, row in enumerate(inner):
        for i in range(1, len(row)-1):
            dist = 1
            for k in range(i+1, len(row)-1):
                if row[k] >= row[i]:
                    break
                dist = dist + 1
            result[row_index+1, i] = dist
    return result


def fill_outer_edges(in_mat):
    in_mat[:,0].fill(1)
    in_mat[:,-1].fill(1)
    in_mat[0, :].fill(1)
    in_mat[-1, :].fill(1)


def calculate_combined_map_part1(trees):
    left = find_visible_trees(trees)

    trees_from_right = np.fliplr(trees)
    right = np.fliplr(find_visible_trees(trees_from_right))

    trees_from_top = np.transpose(trees)
    top = np.transpose(find_visible_trees(trees_from_top))

    trees_from_bottom = np.fliplr(np.transpose(trees))
    bottom = np.flipud(np.transpose(find_visible_trees(trees_from_bottom)))

    combined = np.logical_or(np.logical_or(left, right), np.logical_or(top, bottom))
    return combined


def calculate_combined_map_part2(trees):
    left = calculate_viewing_distance(trees)

    trees_from_right = np.fliplr(trees)
    right = np.fliplr(calculate_viewing_distance(trees_from_right))

    trees_from_top = np.transpose(trees)
    top = np.transpose(calculate_viewing_distance(trees_from_top))

    trees_from_bottom = np.fliplr(np.transpose(trees))
    bottom = np.flipud(np.transpose(calculate_viewing_distance(trees_from_bottom)))

    combined = np.multiply(np.multiply(left, right), np.multiply(top, bottom))
    return combined


if __name__ == "__main__":
    # trees = read_data('example.txt')
    trees = read_data('input.txt')
    combined = calculate_combined_map_part1(trees)
    fill_outer_edges(combined)
    print("PART1 count:", np.count_nonzero(combined))

    combined_scenic = calculate_combined_map_part2(trees)
    highest_scenic_score = combined_scenic.max()
    print("PART2 highest scenic score:", highest_scenic_score)

    # plt.figure()
    # plt.imshow(trees)
    # plt.figure()
    # plt.imshow(combined) # yellow = visible
    # plt.imshow(combined_scenic)
    # plt.show()
