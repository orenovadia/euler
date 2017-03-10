from itertools import chain
from pprint import pprint
from time import time, sleep

from cachetools import cached

test_matrix = [
    [7, 53, 183, 439, 863],
    [497, 383, 563, 79, 973],
    [287, 63, 343, 169, 583],
    [627, 343, 773, 959, 943],
    [767, 473, 103, 699, 303],
]

real_matrix = [
    [7, 53, 183, 439, 863, 497, 383, 563, 79, 973, 287, 63, 343, 169, 583],
    [627, 343, 773, 959, 943, 767, 473, 103, 699, 303, 957, 703, 583, 639, 913],
    [447, 283, 463, 29, 23, 487, 463, 993, 119, 883, 327, 493, 423, 159, 743],
    [217, 623, 3, 399, 853, 407, 103, 983, 89, 463, 290, 516, 212, 462, 350],
    [960, 376, 682, 962, 300, 780, 486, 502, 912, 800, 250, 346, 172, 812, 350],
    [870, 456, 192, 162, 593, 473, 915, 45, 989, 873, 823, 965, 425, 329, 803],
    [973, 965, 905, 919, 133, 673, 665, 235, 509, 613, 673, 815, 165, 992, 326],
    [322, 148, 972, 962, 286, 255, 941, 541, 265, 323, 925, 281, 601, 95, 973],
    [445, 721, 11, 525, 473, 65, 511, 164, 138, 672, 18, 428, 154, 448, 848],
    [414, 456, 310, 312, 798, 104, 566, 520, 302, 248, 694, 976, 430, 392, 198],
    [184, 829, 373, 181, 631, 101, 969, 613, 840, 740, 778, 458, 284, 760, 390],
    [821, 461, 843, 513, 17, 901, 711, 993, 293, 157, 274, 94, 192, 156, 574],
    [34, 124, 4, 878, 450, 476, 712, 914, 838, 669, 875, 299, 823, 329, 699],
    [815, 559, 813, 459, 522, 788, 168, 586, 966, 232, 308, 833, 251, 631, 107],
    [813, 883, 451, 509, 615, 77, 281, 613, 459, 205, 380, 274, 302, 35, 805],
]
M = test_matrix
N = len(M)


def semi_greedy(mat):
    def coordinates_of_n_in_m(m, n):
        for i in xrange(len(m)):
            for j in xrange(len(m)):
                if m[i][j] == n:
                    yield i, j

    def remove_cross_from_mat(m, row, col):
        if len(m) == 1:
            return []
        return [[item for j, item in enumerate(line) if j != col] for i, line in enumerate(m) if i != row]

    def deep_choice_semi_greedy(m, s=0, large_numbers_to_skip=None):
        if not m:
            yield s
            raise StopIteration()

        large_nums = sorted(set(chain.from_iterable(m)) - large_numbers_to_skip, reverse=True)

        for n in large_nums[:2]:
            for i, j in list(coordinates_of_n_in_m(m, n)):
                # print len(m), n, (i, j)
                for option in deep_choice_semi_greedy(remove_cross_from_mat(m, i, j), s + n,
                                                      set(large_numbers_to_skip)):
                    yield option
            large_numbers_to_skip.add(n)

    max_ = 0
    for possible_sum in deep_choice_semi_greedy(mat, 0, set()):
        if max_ < possible_sum:
            max_ = possible_sum
            print max_


def dp_approach(m):
    @cached({})
    def max_for_rows_and_cols(row_indices, col_indices):
        if not row_indices:
            return 0
        # For each column (you haven't taken from), choose the item in the first row you haven't
        # taken from yet -> add it to maximum from remaining matrix
        return max(
            m[row_indices[0]][col] + max_for_rows_and_cols(row_indices[1:], col_indices[:j] + col_indices[j + 1:]) for
            j, col in enumerate(col_indices))

    print max_for_rows_and_cols(tuple(range(len(m))), tuple(range(len(m))))


if __name__ == '__main__':
    st = time()
    dp_approach(real_matrix)
    print 'DP Took ', time() - st
    st = time()
    semi_greedy(real_matrix)
    print 'Semi greedy Took ', time() - st
