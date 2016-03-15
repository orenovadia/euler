'''
Created on Sep 11, 2015
12:16:47 AM
@author: oovadia
'''
from time import time
from eulertools import primes2
import pyprimes
from numpy import prod
N=10**8
pp = primes2(N/2)
pp.pop(0)
lenpp = len(pp)
print 'len',lenpp
sun=0
log = open ( 'log.txt','wb')
muls = lambda x,y: x*y
def mymul(l):
    return reduce(muls,l or [1])
def dive(l,idx):
    global sun,N,mul
    if mymul(l)>N: return
    for i,p in enumerate(l):
        pr =  ( mymul([x for x in l if x!=p]) )
        if not  pyprimes.is_prime(p+pr):
            #l.pop(-1)
            #okay = False
            return
    #if l and okay:
    if l: 
        if len(l)>1:
            log.write( '%s %s \n'% (p*pr,l) )
            sun+=p*pr
            assert prod(l)<N
    for i in xrange(lenpp-idx):
        if prod(l+ [pp[idx+i] ] )>N: return
        dive(l+ [pp[idx+i]  ,],idx+i+1)
        
def run():
    dive([2],0)
    
           
    
if __name__ == '__main__':
    st = time()
    run()
    delta = 4690250
    print sun
    print sun+delta
    print 'time: ',time()-st,'secs'
    