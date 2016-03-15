'''
Created on Mar 9, 2015

@author: oovadia
'''
#from eulertools import primes3,Dn,primeFactors
from time import time as thistime
from math import log,sqrt
from itertools import groupby


def primeFactors(n):
    from itertools import groupby
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
        primfac.append(n)
    return primfac
    #counts = [len(list(group)) for key, group in groupby(factors)]


def s2nMinuss2m(n,m):
    return n*(n+1)*(2*n+1)/6 - m*(m+1)*(2*m+1)/6

def sigmakOfN2(k,n):
    prm = primeFactors(n)
    counts =[ len(list(group)) for key, group in groupby(prm)]
    prm = list(set(prm))
    s=1
    for i,pow in enumerate(counts):
        p = prm[i]
        s *= (p**( (pow+1)*k )-1)/( p**k -1 )
    return s
 
def s2n(n):
    return n*(n+1)*(2*n+1)/6


def run(n):
    r = int(sqrt(n))
    print 'r:',r
    s=0
    ten9=10**9
    i=1
    lastN=n
    end=r
    if r**2==n:
        end-=1
    while i<=end:
        nDivD=n//i
        s%=ten9
        sumSquaresInInterval=s2nMinuss2m(lastN,nDivD) %ten9
        s+=((nDivD)*i**2)+sumSquaresInInterval*(i-1)
        #print i,'\t',s
        i+=1
        lastN = nDivD
    nDivD=n//i
    s%=ten9
    #print 'i,nDivD',i,nDivD
    if i<nDivD:
        sumSquaresInInterval=s2nMinuss2m(lastN,nDivD) %ten9
        s+=((nDivD)*i**2)+sumSquaresInInterval*(i-1)
    elif nDivD==r:
        #
        if r**2==n:
            s+=((nDivD)*i**2)
        sumSquaresInInterval=s2nMinuss2m(lastN,nDivD) %ten9
        s+=sumSquaresInInterval*(i-1)
        
        pass
    print i,'\t',s
    print n,'\t',s%ten9,'\t',s


def calcRealSIGMA2(n):
    s=0
    for i in xrange(1,n+1):
        s+=sigmakOfN2(2,i)
    print n,s 
    return s    
    
    
def main():
    st = thistime()
    run(10**15)
    print 'time: ',thistime()-st,'secs'

if __name__ == '__main__':
    main()