import gmpy2
from bisect import bisect

import eulertools

N = 10 ** 9
p_arr = eulertools.primes3(int(N ** 0.5) + 10)
print 'Number of primes up to sqrt N:', len(p_arr)
p_arr = p_arr[:10]
n_primes = len(p_arr)

bla = []


def generate_all_admissibles(N, current, i_in_p_arr):
    global p_arr, n_primes, bla
    if current > N: return current
    bla.append(current)
    for i in range(i_in_p_arr, i_in_p_arr + 2):
        generate_all_admissibles(N, current * p_arr[i], i)


generate_all_admissibles(N, 2, 0)
print 'number of admissibles:', len(bla)
bla.sort()
print 'sorted'
# 2,4,6,8,12,16,18,24,30,32,36,48
# [2, 4, 6, 8, 12, 16, 18, 24, 30, 32, 36, 48, 54]
counts = set()
for i in bla:
    ind = bisect(p_arr, i)
    if ind >= n_primes:
        next_prime = gmpy2.next_prime(i)
    else:
        next_prime = p_arr[ind]
    if next_prime - i == 1:
        next_prime = gmpy2.next_prime(next_prime)
    M = int(next_prime) - i
    counts.add(M)
    
print len(counts), len(bla)
print 'Max M', max(counts)
# print counts
print 'finished , sum of psuedo luckys:', sum(counts)
