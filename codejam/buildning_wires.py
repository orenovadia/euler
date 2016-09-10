import itertools

from numpy.core.umath import sign


class Problem(object):
    def __init__(self, n_wires, wire_tuples):
        self.wire_tuples = wire_tuples
        self.n_wires = n_wires

    def solve(self):
        s=0
        print 'solvinf for ', self.n_wires
        for wire1, wire2 in itertools.combinations(self.wire_tuples, r=2):
            left =  wire1[0] -  wire2[0]
            right =  wire1[1] -  wire2[1]
            if right == 0 or left == 0:
                continue
            if sign(left) != sign(right):
                s+=1
        return s


with open('A-small-practice.in', 'rb') as f, open('sol.out', 'wb') as out:
    n = int(f.readline())
    for case in range(1, n + 1):
        n_wires = int(f.readline())
        wires_tuples = []
        for j in range(n_wires):
            t = tuple(map(int, f.readline().split()))
            wires_tuples.append(t)
        solve = Problem(n_wires, wires_tuples).solve()
        print >> out, 'Case #{}: {}'.format(case, solve)
