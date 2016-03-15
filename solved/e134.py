'''
Created on Mar 18, 2015
8:08:47 PM
@author: oovadia
'''
from time import time
from eulertools import primes3
from pyprimes import next_prime

def is_right(p1,num):
    s1 =str(p1)
    if s1 == str(num)[-len(s1):]:
        return True
    return False

def run(n):
    #n=10**6
    l = primes3(10**6)
    l+= [next_prime(l[-1])]
    print l[-3:]
    s=0 
    print len(l)   
    for i in xrange(len(l)-2,len(l)-1):
        p1,p2 = l[i],l[i+1]
        #print p1,p2
        mul =1
        m=p2
        while not is_right(p1, m):
            m+=p2
        print p1,p2,m,m/p2
        #print p1
        s+=m
    print s
       
def main(n): 
    st = time()
    run(n)
    print 'time: ',time()-st,'secs'
    
if __name__ == '__main__':
    main(100)
    