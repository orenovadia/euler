from math import log,sqrt
from eulertools import primes3
from _bisect import bisect

prm = primes3(10**6)
print prm[-1]


def isCube(x):
    t = x**(1.0/3)
    t = int (t)
    t3 = t**3
    if t**3==x or (t+1)**3==x:
        return True
    return False

count = 0
idx = bisect(prm, 100)
idx = len(prm)
lastprime = 0
for n in xrange(1,1000):
    n=n**3
    N3=n**3
    N2=n**2
    
    pind = lastprime
    p=prm[pind]
    while p<prm[-1]:
        p=prm[pind]
        X3 = N2*(n+p)
        if isCube(X3):
            count+=1
            print p,n,X3**0.33334,'\t',count
            lastprime = pind
            break
        pind+=1
 
print count
'''for p in prm[:100]:
    for n in xrange(1,1000):
        x=n**2 * (n+p)
        if isCube(x):
            print 'p:',p,'\t\tn:',n,'\t\tx',x**(1.0/3)
            count+=1
            break
'''

