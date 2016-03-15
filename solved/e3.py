'''
Created on Mar 27, 2015
6:14:32 PM
@author: oovadia
'''
from time import time
from eulertools import primes3,primeFactors
def run():
    f = primeFactors(600851475143 )
    print max(f)
    print f
    

if __name__ == '__main__':
    st = time()
    #run()
    for i in range(0):
        print i 
    else:
        print 'none'
    print 'time: ',time()-st,'secs'
    