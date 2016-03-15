'''
Created on Feb 26, 2015

@author: oovadia
'''
from eulertools import primeFactors

N=20
l = [0] * N

for i,k in enumerate(l):
    p = primeFactors(i)
    print i, len(p) , p
