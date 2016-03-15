from eulertools import Dn,primeFactors
from itertools import groupby,combinations
from math import log,sqrt,factorial

N=10000
minimal = N
'''from eulertools import primes
prm = primes(N/6)
print prm 
exit(0)
'''
filename = 'primes%d.txt' % (N/6)
#prm =[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163]
with open (filename,'rb') as f:
    prm = eval(f.read())


'''
Allowed Permutations:
1,1,1
3,1
7
'''
#print prm

nPrm =  len ( prm )


def calcNum(l,prm):
    s=1
    for i,pows in enumerate(l):
        s*=prm[i]**pows
    return s
prevFactors=0
previ=0
prev=[]
goal=4
for i in xrange(500,10**6):
    f=primeFactors(i)
    curf = len(set(f))
    if curf==prevFactors and curf == goal:
        print previ,i,
        prev.append(previ)
        if len(prev)==goal-1:
            print 
            print prev ,curf,f  
            break
    else:
        prev=[]
    previ,prevFactors=i,curf
