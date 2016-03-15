'''
Created on Mar 27, 2015
6:06:31 PM
@author: oovadia
'''
from time import time

def s(n_n):
    return (n_n)*(n_n+1)/2

def SxSy(x,y):
    return s(x)*s(y)

def dist(x,y,target):
    return abs( SxSy(x,y) - target  )

def run():
    target =2*10**6
    x=10
    y=300   
    area ,combos = 0 , 10000000
    print SxSy(x, y)
    for x in xrange(5,55):
        for y in xrange(x+1,400):
            if dist(x, y, target)< combos:
                area ,combos = x*y , dist(x, y, target)
                print area ,combos ,x,y
    print area ,combos 

if __name__ == '__main__':
    st = time()
    run()
    print 'time: ',time()-st,'secs'
    