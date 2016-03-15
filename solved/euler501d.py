from eulertools import Dn,primeFactors,primes2
from itertools import groupby,combinations
from math import log,sqrt,factorial
from bisect import bisect_left
N=1666
tt=N
minimal = N
'''from eulertools import primes
prm = primes(N/6)
print prm 
exit(0)
'''


'''
Allowed Permutations:
1,1,1
3,1
7
'''
a

#print prm
goals = (2,3,4,5,6,7,8,9,10)
nsolss = [0 for i in goals]
nSols = 0
for i in xrange(2,N+1):
    print i
    d = primeFactors(i)
    counts = [len(list(group)) for key, group in groupby(d)]
    nDivisors = Dn(counts)
    if nDivisors in goals:
        nsolss[ bisect_left(goals, nDivisors) ]+=1
for i,goal in enumerate(goals):
    print 'Numbers under %d with %d divisors: %d' % (N,goal,nsolss[i])
for powa in (2,3,4,5,6,7):
    for N in (tt,):    
        prm =primes2(int(N**0.5)+2)
        aPow7=0
        for i in prm:
            if i**powa<=N:
                aPow7+=1
            else: break
        print 'Numbers under %d like Pk^%d: %d' % (N,powa,aPow7)
for powa in (2,3,4,5,6,7):
    for N in (tt,):    
        prm = primes2(N/6)  
        nSols = 0
        for i in prm:
            i3=i**powa
            for j in prm:
                if i3*j>N: break
                elif i!=j: 
                    nSols+=1
                    #print i,j
        print 'Numbers under %d like a^%d*b: %d' % (N,powa,nSols)