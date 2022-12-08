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


def for_all_rows(in_mat):
    result = np.zeros_like(in_mat)
    for row_index, row in enumerate(in_mat[1:-1, :]):
        for i in range(1, len(row)-1):
            # print(row_index+1, i, row[i] > max(row[:i]), row[:i+1])
            if row[i] > max(row[:i]):
                result[row_index+1, i] = 1
    return result


def fill_outer_edges(in_mat):
    in_mat[:,0].fill(1)
    in_mat[:,-1].fill(1)
    in_mat[0, :].fill(1)
    in_mat[-1, :].fill(1)


def calculate_combined_map(trees):
    left = for_all_rows(trees)

    trees_from_right = np.fliplr(trees)
    right = for_all_rows(trees_from_right)

    trees_from_top = np.transpose(trees)
    top = np.transpose(for_all_rows(trees_from_top))

    trees_from_bottom = np.fliplr(np.transpose(trees))
    bottom = np.flipud(np.transpose(for_all_rows(trees_from_bottom)))

    combined = np.logical_or(np.logical_or(left, right), np.logical_or(top, bottom))
    return combined


if __name__ == "__main__":
    # trees = read_data('example.txt')
    trees = read_data('input.txt')
    print("input shape:", np.shape(trees))
    combined = calculate_combined_map(trees)
    fill_outer_edges(combined)
    print("count:", np.count_nonzero(combined))

    # plt.figure()
    # plt.imshow(trees)
    plt.figure()
    plt.imshow(combined) # yellow = visible
    plt.show()
