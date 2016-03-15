'''
Created on Mar 26, 2015
8:22:07 AM
@author: oovadia
'''
from time import time

def run():
    n_n=1000
    m=10**10
    s=0
    for i in xrange(1,n_n+1):
        ad=1
        for j in xrange(i):
            #if i==3: print j
            ad*=i
            ad%=m
        s+=ad
    print s%m
    

if __name__ == '__main__':
    st = time()
    run()
    print 'time: ',time()-st,'secs'
    