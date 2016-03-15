'''
Created on Mar 16, 2015
8:55:08 PM
@author: oovadia
'''
from time import time
import numpy as np


A = np.array([ [1,-2,2],[2,-1,2],[2,-2,3]  ])
B = np.array( [ [1, 2,2],[2, 1,2],[2, 2,3]  ])
C = np.array( [ [-1,2,2],[-2,1,2],[-2,2,3]  ])

s = 0
maxPerimiter=10**9
import sys
sys.setrecursionlimit(200000)
def run(v,mat):
    global s,maxPerimiter 
    a,b,c = v 
    a2,b2 = a*2,b*2
    peri = min(a2+2*c,b2+2*c)


    if a2+1==c or a2-1==c:
        peri = (a2+2*c)
        if peri>maxPerimiter: 
            return
        s+=peri
        print 'a',mat,v#,a2,c
    elif b2+1==c or b2-1==c:
        peri = (b2+2*c)
        if peri>maxPerimiter: 
            return
        s+=peri
        print 'b',mat,v#,b2,c
    else:
        pass 
        #return
        
    if mat=='A':
        run( np.dot(C,v),'C'  )
    else:
        run( np.dot(A,v),'A'  )
    #run( np.dot(B,v),'B'  )
    
    
def main():
    st = time()
    global s
    s=0
    run(np.array([3,4,5]),'A')
    print s
    print ('time: ',time()-st,'secs')

if __name__ == '__main__':
    st = time()
    global s
    s=0
    run(np.array([3,4,5]),'A')
    print s
    print ('time: ',time()-st,'secs')
 