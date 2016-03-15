'''
Created on Mar 9, 2015

@author: oovadia
'''
from time import time as thistime
from math import log
from eulertools import primes3,Dn


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
    
    

def run(powDiv=8):
    nDiv = 2**powDiv
    prm = primes3(7376520)
    nprm = len(prm)
    pows = [1 for i in xrange (powDiv)]
    #print pows
    min = calcNum(pows, prm)
    while True:
        pass
        #print i,calcNum(pows, prm),Dn(pows),pows
        primeInGame = len(pows)
        p = prm [primeInGame]
        print 'poped:',p
        powLast = pows.pop(-1)
        if powLast!=1: assert powLast,p
        ratMin=2
        iMin=None
        for i in xrange(primeInGame-1):
            q = prm[i]
            lastPow = pows[i]
            newPow  = advance2Powers(lastPow)

            if q**(newPow-lastPow)>p:
                continue
            else:
                rat = 1.0/p*q**(newPow-lastPow)
                #print q**(newPow-lastPow)>p,rat
                if rat<ratMin:
                    ratMin=rat
                    iMin=i
                elif lastPow==1:
                    pass
                    break
                    
        if ratMin<1:
            pows[iMin] = advance2Powers(pows[iMin])
        else:
            pows.append(powLast)
            print 'minimal:',calcNum(pows, prm),pows[:100] ,iMin
            print 'minimal:',calcNum(pows, prm)
            break

    
def main(x):
    st = thistime()
    run(x)
    print 'time: ',thistime()-st,'secs'

if __name__ == '__main__':
    main(500500)