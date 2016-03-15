'''
Created on Mar 19, 2015
11:44:00 PM
@author: oovadia
'''
from time import time
from eulertools import primes3,arePermutations


def totient(p1,p2):
    return (p1-1)*(p2-1)

def run():
    limit = 10**7
    prm = primes3(10**6)
    minN=0
    minNdivPhiN=limit*1.
    for ind,p1 in enumerate(prm[:1000]):
        for p2 in prm[ind+1:]:
            n = p1*p2
            if n>limit: break
            phiN = totient(p1, p2)
            if arePermutations(n, phiN):
                if minNdivPhiN>n*1.0/phiN:
                    minNdivPhiN=n*1.0/phiN
                    minN=n
                    print p1,p2,minN,minNdivPhiN
            

if __name__ == '__main__':
    st = time()
    run()
    print 'time: ',time()-st,'secs'
    