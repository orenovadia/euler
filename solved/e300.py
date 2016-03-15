'''
Created on Sep 11, 2015
12:16:47 AM
@author: oovadia
'''
from time import time
N=8
total_sum = 0
#returns number of combinations
def dive(touches,steps,total_steps,n_H,n_H_placed,target_touches):
    if steps==N: return 0
    if n_H==n_H_placed: return 0
    for my_spot in range(steps,N):
        print my_spot

def run():
    for n_H in range(0,N+1):
        print 'number of H:',n_H
        dive(0, 0, 0, n_H,0, 0)    
    

if __name__ == '__main__':
    st = time()
    run()
    print 'time: ',time()-st,'secs'
    