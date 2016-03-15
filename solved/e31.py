'''
Created on Mar 20, 2015
8:58:07 PM
@author: oovadia
'''
from time import time,sleep
from test.test_decorators import memoize
coins = [1,2,5,10,20,50,100,200]
limit = 200
nCoins = len(coins)
shapes = 0
def calcAmount(a):
    global coins
    s=0
    for amountOf,coin in zip(a,coins):
        s += amountOf*coin
    return s

def run(a,ind):
    global coins,limit,nCoins,shapes
    if ind >= nCoins: return
    s=0
    #print a
    s = calcAmount(a)
    while True:
        if s>limit:
            a[ind] = 0
            return
        elif s<limit:
            run(a,ind+1)
        else:
            shapes+=1
            #print a
            a[ind] = 0
            return
        a[ind] = a[ind] +1
        s = calcAmount(a)
    a[ind] = 0
    return

def nway( total, coins):
    if not coins: return 0
    c, coins = coins[0], coins[1:]
    count = 0 
    if total % c == 0: count += 1    
    for amount in xrange( 0, total, c):
        count += nway(total - amount, coins)    
    return count
# main


if __name__ == '__main__':
    st = time()
    s = [0] * len(coins)
    run(s,0)
    #print nway( 200, (1,2,5,10,20,50,100,200))
    print shapes
    print 'time: ',time()-st,'secs'
    
    