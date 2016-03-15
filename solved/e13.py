'''
Created on Mar 20, 2015
8:37:17 PM
@author: oovadia
'''
from time import time


def run():
    s=0
    with open('prob13.txt') as f:
        for row in f:
            s+= int(row )
    print s
    

if __name__ == '__main__':
    st = time()
    run()
    print 'time: ',time()-st,'secs'
    