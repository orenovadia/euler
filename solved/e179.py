'''
Created on Mar 21, 2015
3:37:18 PM
@author: oovadia
'''
from eulertools import sigma0, primes3
from time import time
from fractions import gcd

def run():
    n=10**7
    l = [1]*(n+1)
    for i in xrange(2,n): 
        for j in xrange(i,n,i):
            l[j] += 1


    s=0    
    for i in xrange(1,n):
        if l[i]==l[i+1]:
            s+=1
    print s

if __name__ == '__main__':
    st = time()
    run()
    print 'time: ',time()-st,'secs'
    