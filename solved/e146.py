'''
Created on Mar 28, 2015
1:44:09 PM
@author: oovadia
'''
from time import time
from bisect import bisect
from eulertools import primesfrom2to,primes3,primeFactors, primes2
from pyprimes import is_prime
from random import randint


x =  len(primes2(10000000-1)) - len(primes2(1000000))
print 1.0*x/ (10000000-1000000)
print len(primes2(1000000))