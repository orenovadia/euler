'''
Created on Mar 18, 2015
4:51:08 PM
@author: oovadia
'''
from time import time
import pyprimes
import pickle
import itertools

def run():
    n_n=10**14
    p=[]
    for i in xrange(100001):
        n_n=pyprimes.next_prime(n_n)
        p.append(n_n)
    with open('primes304.txt','wb') as f:
        pickle.dump(p, f)
    print n_n
 
def nFib():
    a=0
    b=1
    mod = 1234567891
    i=0
    while b!=0:
        i+=1
        a,b = b,a+b
        b%=mod
        if b==0:
            print a,b,i 
            break


    print(a,b)

if __name__ == '__main__':
    st = time()
    nFib()
    print 'time: ',time()-st,'secs'
    