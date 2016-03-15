from eulertools import primes,primes2
from math import sqrt

N=10**12
N=int(sqrt(N))*10
filename = 'primes%d.txt' % (N)
with open(filename,'wb') as f:
    f.write(str(primes2(N)))
print 'All Primes smaller than N: ',filename