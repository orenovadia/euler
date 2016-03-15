'''
Created on Mar 20, 2015
8:42:17 PM
@author: oovadia
'''
from time import time

def collatzNext(n):
    if n%2==0:
        return n/2
    else:
        return 3*n+1

def run(n):
    cach = [-1]*(2*n+1)
    numInCache=len(cach)-1
    for i in xrange(1,n+1):
        num=i
        count =1
        while num!=1:
            count+=1
            num = collatzNext(num)
            if num<numInCache:
                if cach[num]!=-1:
                    count+=cach[num]-1
                    break
                    pass
                else:
                    pass
                    #cach[num]=count
        cach[i]=count
    M=max(cach)
    import numpy
    for n,i in enumerate(cach):
        if i == M:
            print n 
            return
        
if __name__ == '__main__':
    st = time()
    run(1000000)
    print 'time: ',time()-st,'secs'
    