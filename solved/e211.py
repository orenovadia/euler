'''
Created on Mar 9, 2015

@author: oovadia
'''
from time import time as thistime
from math import log,sqrt
from eulertools import primes3,Dn,primeFactors
from itertools import groupby


def calcNum(l,prm):
    s=1
    for i,pows in enumerate(l):
        s*= ( prm[i]**pows )
        s%=500500507
    return s

def advance2Powers(n):
    n+=1
    t = int( log(n,2))+1
    return 2**t-1
    
def sigmakOfN(k,n,prm,l):
    s=1
    for i,pow in enumerate(l):
        p = prm[i]
        s *= (p**(pow+1) -1)/( p -1 )
    return s

def sigmakOfN2(k,n):
    prm = primeFactors(n)
    counts =[ len(list(group)) for key, group in groupby(prm)]
    prm = list(set(prm))
    s=1
    for i,pow in enumerate(counts):
        p = prm[i]
        s *= (p**( (pow+1)*k )-1)/( p**k -1 )
    return s
 
 
def is_square(apositiveint):

    x = apositiveint // 2
    seen = set([x])
    while x * x != apositiveint:
        x = (x + (apositiveint // x)) // 2
        if x in seen: return False
        seen.add(x)
    return True

def is_square2(apositiveint):
    tmp = long(apositiveint**0.5)
    if tmp**2==apositiveint: return True
    if (tmp+1)**2==apositiveint: return True
    if (tmp-1)**2==apositiveint: return True
    return False
    
def run(n):

    l = [1]*(n+1)
    for i in xrange(2,n+1): 
        for j in xrange(i,n,i):
            l[j] += i**2

    print 'creating dict:'
    s=1
    l[0]=0
    l[1]=1
    d = {}
    for num, x in enumerate(l):
        d[x]=d.get(x,0)+num
    print l[:10]
    maxSig = max(l)
    print 'maxSig',maxSig
    i=2
    i2=4
    while i2<=maxSig:
        s+= d.get(i2,0)
        i+=1
        i2=i**2
    print s
    
def runOld(n):
    s=1
    for i in xrange(2,n):
        s2 = sigmakOfN2(2,i)
        if is_square(s2):
            t = primeFactors(i)
            print i,s2,s2**0.5,t,sum(t)
            s+=i
    print s

def main(x):
    st = thistime()
    run(x)
    print 'time: ',thistime()-st,'secs'

if __name__ == '__main__':
    main(64*1000000)