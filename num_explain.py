#!/usr/bin/python
'''
python num_explain.py 13
will print information about 13
@author: oren
'''
import gmpy2
import itertools
import sys

import eulertools


def analyze_number(n):
    print 'Number          %-15s' % n
    print 'Prime           %-15s' % gmpy2.is_prime(n)
    print 'Is square       %-15s' % ((n ** 0.5) == n)
    print 'Square root     %-15s' % (n ** 0.5)
    print 'Cube   root     %-15s' % (n ** (1.0 / 3.0))
    print 'Sum of digits   %-15s' % eulertools.sum_of_digits(n)
    print 'Prime factors   %-15s' % eulertools.primeFactors(n)
    print '# Factors       %-15s' % len(eulertools.divisorGenerator(n))
    print 'Factors         %-15s' % eulertools.divisorGenerator(n)


if __name__ == '__main__':
    numbers = [int(i) for i in sys.argv[1:]]
    print '%' * 50
    for n in numbers:
        analyze_number(n)
        print '-' * 50
    print '%' * 50
    for a, b in itertools.combinations(numbers, 2):
        print 'GCD             %-14s %-14s: %s' % (a, b, gmpy2.gcd(a, b))
        print 'Permutations    %-14s %-14s: %s' % (a, b, eulertools.arePermutations(a, b))
        print '-' * 50
    print '%' * 50

