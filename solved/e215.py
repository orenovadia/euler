from collections import defaultdict
from itertools import combinations_with_replacement

import numpy as np
from cachetools import cached
from numpy import linalg as liniag

from euler.eulertools import unique_permutations

DT = np.int64
ANY_LAYER = None


def cum_sum(l):
    s = 0
    cum_sum_list = []
    for i in l:
        s += i
        cum_sum_list.append(s)
    return cum_sum_list


class NewPermutations(object):
    bricks = (2, 3)
    min_brick = min(bricks)

    def __init__(self, width):
        super(NewPermutations, self).__init__()
        self.width = width
        self.permutations = list(self._create_permutations(width))
        self.n = len(self.permutations)
        self.crack_places = map(self._bricks_to_crack_sets, self.permutations)

    @staticmethod
    def _bricks_to_crack_sets(permutation):
        crack_set = set()
        s = 0
        for brick in permutation[:-1]:
            s += brick
            crack_set.add(s)
        return crack_set

    def _create_permutations(self, width):
        if width in self.bricks:
            yield (width,)
        elif width < self.min_brick:
            raise StopIteration()
        for brick in self.bricks:
            for possible_rest_of_layer in self._create_permutations(width - brick):
                yield (brick,) + possible_rest_of_layer


class _Permutations(object):
    def __init__(self, width):
        self.width = width
        self.possibilities = self._create_possibilities(width)
        print 'finished possibilities, got:', len(self.possibilities)
        self.permutations = self._create_permutations(self.possibilities)
        self.n = len(self.permutations)
        print 'finished permutations, got:', self.n
        assert all(sum(p) == width for p in self.permutations)
        self.crack_places = self._crack_places(width)
        print 'finished crack places'

    def _crack_places(self, width):
        crack_places = map(set, map(cum_sum, self.permutations))
        for crack_place in crack_places:
            crack_place.remove(width)
        return crack_places

    def _iter_combinations(self, width):
        max_bricks = width / 2
        min_bricks = width / 3
        for i in range(min_bricks, max_bricks + 1):
            for combination in combinations_with_replacement([2, 3], r=i):
                yield combination

    def _create_possibilities(self, width):
        possibilities = []
        for combination in self._iter_combinations(width):
            if sum(combination) == width:
                possibilities.append(combination)
        return possibilities

    def _create_permutations(self, possibilities):
        perms = set()
        for possibility in possibilities:
            for p in unique_permutations(possibility):
                perms.add(p)
        return list(perms)


Permutations = NewPermutations

class LGraph(object):
    def __init__(self, n):
        super(LGraph, self).__init__()
        self.mat = np.zeros((n, n), dtype=DT)

    def add_edge(self, i, j):
        self.mat[i, j] = 1
        self.mat[j, i] = 1

    def power(self, p):
        return liniag.matrix_power(self.mat, p)


class NGraph(object):
    def __init__(self, n):
        super(NGraph, self).__init__()
        self.n = n
        self._neighbors = defaultdict(set)
        self._neighbors[ANY_LAYER] = set(xrange(n))

    def add_edge(self, i, j):
        self._neighbors[i].add(j)
        self._neighbors[j].add(i)

    def neighbors_of(self, i):
        return self._neighbors[i]


def main(width, height):
    # create layer permutations
    p = Permutations(width)
    solve_with_dp(height, p)
    # solve_with_matrix(height, p)


@cached(dict())
def ways(g, layer, height):
    if height == 0:
        return 1
    ss = 0
    for l in g.neighbors_of(layer):
        ss += ways(g, l, height - 1)
    return ss


def solve_with_dp(height, p):
    g = NGraph(p.n)
    populate_graph(g, p)
    print 'solutions cached:', ways(g, ANY_LAYER, height)


def solve_with_matrix(height, p):
    g = LGraph(p.n)
    populate_graph(g, p)
    print 'finished populating graph'
    print 'Powering up matrix'
    matrix_power = g.power(height - 1)
    print 'Upped matrix by power'
    print 'Ways:', matrix_power.sum()


def populate_graph(g, p):
    crack_places = p.crack_places
    n = len(crack_places)
    for i in xrange(n):
        for j in xrange(i, n):
            matching_cracks = crack_places[i].intersection(crack_places[j])
            if len(matching_cracks) == 0:
                g.add_edge(i, j)


if __name__ == '__main__':
    main(9, 3)
    main(32, 10)
