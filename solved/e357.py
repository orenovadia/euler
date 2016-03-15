'''
Created on Mar 26, 2015
6:58:58 PM
@author: oovadia
'''
from time import time
from eulertools import primes3,divisorGenerator, primeFactors
#from pyprimes import is_prime
from itertools import combinations
from _bisect import bisect
'''def checkNum(l):
    ret = True
    if type(l)==int: return is_prime(l)
    for p in l:
        rest = reduce(lambda x,y:x*y , [q for q in l if q!=p])
        ret = ret and is_prime(p + rest)
    return ret

def checkN(N):
    dlist = divisorGenerator(N)
    return all(is_prime(d+N/d) for d in dlist)
'''
def checkN2(N,prm):
    dlist = divisorGenerator(N)
    return all( (d+N/d) in prm for d in dlist)

limit = 0
'''def nway( total, coins):
    global limit
    if not coins: 
        return 0
    c, coins = coins[0], coins[1:]
    count = 0 
    new = total*c 
    if new<limit and checkN(new):
        count+=new  
        print new
        count+=nway(new , coins)
    if total<limit:
        count+=nway(total, coins)


    return count  
 
def run():

    n_n=1000
    global limit
    limit  = n_n
    prm = primes3(n_n/2+1)[1:]
    l = len(prm)
    print l

    print 'nway:',nway(2,prm)+2+1


def buildIt(n_n=1000):
    global limit
    limit  = n_n
    prm = primes3(n_n/2+1)[1:]
    candidates = []
    for p in prm:
        if is_prime(p+2):
            if (p*2)<n_n:
                if is_prime(p*2+1):
                    candidates.append(p*2)
    for c in candidates:
        facs = primeFactors(c)
        for p3 in prm[:]:
            if p3 in facs: continue
            nn = p3*c
            if nn == 442: print c,p3
            if nn>n_n: break
            elif checkN(nn):
            #elif is_prime(p3+c):
                candidates.append(nn)
    candidates = sorted( set(candidates) )

    for c in candidates:
        print c , primeFactors(c)
    print sum(candidates)+3
'''    
def bruteIt(n_n=1000):
    st = time()
    s=0
    prm = primes3(n_n)
    for i in xrange(1,n_n):
        if i%(n_n/10000)==1: print i
        if checkN2(i,prm):
            s+=i
    print 'n_n=',n_n,'s=',s
    print 'time: ',time()-st,'secs'
if __name__ == '__main__':
    st = time()
    #run()
    bruteIt()


    print 'time: ',time()-st,'secs'
    