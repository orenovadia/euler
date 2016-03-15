'''
Created on Mar 13, 2015
10:37:36 PM
@author: oovadia
'''
from time import time
from eulertools import primes3
from pyprimes import is_prime, __author__
from itertools import combinations,groupby
from collections import Counter
import __future__
import eulertools


def run(N=100):
    prm = primes3(N)
    nprm = len(prm)
    countNo=0
    countYes=0
    l=[]
    for i,j,k in combinations(prm,3):
        p = i+j+k 
        if p in prm:
            countYes+=1
            l.append(p)
        elif is_prime(p):
            countYes+=1
            l.append(p)
        else:
            countNo+=1
    print countNo,countYes
    l = sorted(l)
    for key,j in groupby(l):
        print key,'\t',len( list(j))
    print l
    print len(l),len(set(l))

if __name__ == '__main__':
    
    st = time()
    run()
    print dir(eulertools)
    print 'time: ',time()-st,'secs'
    