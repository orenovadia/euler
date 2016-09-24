from collections import defaultdict
from itertools import combinations_with_replacement

from cachetools import cached
from numpy import linalg as liniag
from pprint import pprint

import numpy as np

DT = np.int64


def cum_sum(l):
    s = 0
    cum_sum_list = []
    for i in l:
        s += i
        cum_sum_list.append(s)
    return cum_sum_list


class unique_element:
    def __init__(self, value, occurrences):
        self.value = value
        self.occurrences = occurrences


def perm_unique(elements):
    eset = set(elements)
    listunique = [unique_element(i, elements.count(i)) for i in eset]
    u = len(elements)
    return perm_unique_helper(listunique, [0] * u, u - 1)


def perm_unique_helper(listunique, result_list, d):
    if d < 0:
        yield tuple(result_list)
    else:
        for i in listunique:
            if i.occurrences > 0:
                result_list[d] = i.value
                i.occurrences -= 1
                for g in perm_unique_helper(listunique, result_list, d - 1):
                    yield g
                i.occurrences += 1


class Permutations(object):
    def __init__(self, width):
        self.width = width
        self.possibilities = self._create_possibilities(width)
        print 'finished possibilities, got:', len(self.possibilities)
        pprint(self.possibilities)
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
            for p in perm_unique(possibility):
                perms.add(p)
        return sorted(perms)


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
    if layer == -1:
        neigh = xrange(g.n)
    else:
        neigh = g.neighbors_of(layer)
    ss = 0
    for l in neigh:
        ss += ways(g, l, height - 1)
    return ss


def solve_with_dp(height, p):
    g = NGraph(p.n)
    populate_graph(g, p)
    print 'solutions cached:', ways(g, -1, height)


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
