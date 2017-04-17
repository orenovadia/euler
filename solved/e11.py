from itertools import product
from timeit import timeit

import numpy as np
from cachetools import cached
from rx import Observable


def mul_many(l):
    s = 1
    for i in l:
        s *= i
    return s


@cached({})
def _load():
    with open('e11_mat.txt') as f:
        return tuple(tuple(map(int, row.strip().split())) for row in f)


def main():
    ll = _load()
    mm = np.array(ll)
    maximum_prod = 0

    def diagonal(n, m, n_axis, m_axis):
        res = []
        try:
            for x in range(4):
                res.append(mm[n + x * n_axis][m + x * m_axis])
            return res
        except IndexError:
            return 0,

    for i, j in product(range(mm.shape[0]), range(mm.shape[1])):
        maximum_prod = max(maximum_prod, mul_many(diagonal(i, j, 0, 1)))  # -
        maximum_prod = max(maximum_prod, mul_many(diagonal(i, j, 1, 0)))  # |
        maximum_prod = max(maximum_prod, mul_many(diagonal(i, j, 1, -1)))  # /
        maximum_prod = max(maximum_prod, mul_many(diagonal(i, j, 1, 1)))  # \

    print(maximum_prod)


def main_reactive():
    ll = _load()
    mm = np.array(ll)

    def diagonal(n, m, a):
        (n_axis, m_axis) = a
        res = []
        try:
            for x in range(4):
                res.append(mm[n + x * n_axis][m + x * m_axis])
            return res
        except IndexError:
            return 0,

    axes = (
        (0, 1),
        (1, 0),
        (1, -1),
        (1, 1),
    )

    Observable.from_(product(range(mm.shape[0]), range(mm.shape[1]), axes)). \
        map(lambda t: diagonal(*t)) \
        .map(mul_many) \
        .max() \
        .subscribe(print)


if __name__ == '__main__':
    _load()
    print(timeit(main, number=1))
    print(timeit(main_reactive, number=1))
