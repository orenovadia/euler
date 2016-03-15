'''
Created on Apr 11, 2015
8:53:23 AM
@author: oovadia
'''
from time import time
from eulertools import primes3
from bisect import bisect
from math import sqrt
from numpy import where

def checkNum(p,prm):
    print p

def primes(N):
    from numpy import where
    alls = [True]*(N+1)
    for i in xrange(2,int ( sqrt(N) )+1):
        if alls[i]:
            for j in xrange(N):
                m=i**2+i*j
                if m>N: break
                alls[m]=False
    for i in xrange(2,int ( (N) )+1):
        if alls[i]:
            for j in xrange(N):
                m=i+2*j**2
                if m>N: break
                alls[m]=False
    alls[0],alls[1] = [False]*2
    for k,v in enumerate(alls):
        alls[k]=not v
    for k,v in enumerate(alls):
        if   alls[k]:
            if k%2==1:
                print k  
        
    primes = where( alls)[0]
    numP= len(primes)
    print 'Number o primes' ,numP
    return list(primes)


def run():
    n=10000
    N=n
    prm = primes3(n)
    alls = [True]*(n+1)
    for i in prm:
        for j in xrange(N):
            m=i+2*j**2
            if m>N: break
            alls[m]=False
        alls[i]=False
    for i in xrange(0,2,n):
        alls[i]=False
    
    ans = where( alls)[0]
    for p in ans : 
        if p%2==1:
            print(p) 
    
    

if __name__ == '__main__':
    st = time()
    run()
    print 'time: ',time()-st,'secs'
    