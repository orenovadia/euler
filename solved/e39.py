from collections import defaultdict

import numpy as np

A = np.asarray([
    [1, -2, 2],
    [2, -1, 2],
    [2, -2, 3]])
B = np.asarray([
    [1, 2, 2],
    [2, 1, 2],
    [2, 2, 3]])
C = np.asarray([
    [-1, 2, 2],
    [-2, 1, 2],
    [-2, 2, 3]])
v0 = np.asarray((3, 4, 5))

matrices = (A, B, C)


def yield_triangles_up_to(v, p):
    if v.sum() <= p:
        yield v
        for i in range(2, p):
            v_multiplied = v * i  # triangles are not primitive so for 3,4,5 -> 6,8,10 is also right
            if v_multiplied.sum() <= p:
                yield v_multiplied
            else:
                break
        for mat in matrices:
            for triangle in yield_triangles_up_to(mat.dot(v), p):
                yield triangle


def main(p):
    solutions = defaultdict(int)
    for triangle in yield_triangles_up_to(v0, p):
        solutions[triangle.sum()] += 1
    print solutions
    max_solution = max(solutions.values())
    print [k for k in solutions if solutions[k] == max_solution], '=>', max_solution


if __name__ == '__main__':
    main(1000)
