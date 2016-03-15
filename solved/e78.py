#!/usr/bin/python
import sys
import logging
logging.basicConfig(filename='example.log',level=logging.DEBUG,filemode='w',)
g_cashe = {}
import  scipy.misc
def nck(n,k):
    return int( scipy.misc.comb(n,k))
def iterate(N,maxn):
    s=1
    if (N,maxn) in g_cashe: return g_cashe[ (N,maxn) ]
    for i in range(1,  min(N,maxn)):
        #print i, N//i , N-i
        s+= iterate(N-i,
                    min(i,N-i)
                        )
    g_cashe[ (N,maxn) ] = s
            #logging.info('%s %s',N,maxn)
    return s
def divisorGenerator(n):
    l=[]
    for i in xrange(1,n/2+1):
        if n%i == 0: l.append(i)
    l.append(n)
    return l
def num_of_ones_to_add(n):
    s =(n-2)-(n//2)-(n%2)+1
    return s
    if s>0:
        return s+num_of_ones_to_add(n-2)
    else:
        return 0

def smart_build(N):
    d=[0 for i in range(N+1)]
    d[0]=0
    d[1]=1
    d[2]=2
    for i in range(3,N+1):
        d[i] = d[i-1]+1
        if i==4: d[i]+=1

        for j in range(i-2,i//2,-1  ):
            print 'hi ',i,j
            d[i] +=  d[j] - d[j-1]
        print i,d[i]

def naive_main():
    for i in range(50):
        ret =iterate(i,i)
        print i,ret
        sys.stdout.flush()
        #for a,b in g_cashe.items():
#print a,b#,divisorGenerator(b)
smart_build(7)
#naive_main()
#for n in range(7):
#print n , num_of_ones_to_add(n)
