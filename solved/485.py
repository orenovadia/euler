from eulertools import primes2,primeFactors,Dn
from itertools import groupby,permutations
from bisect import bisect

def divisors(x):
    global prm
    if x in prm: return 2
    d = primeFactors(i)
    counts = [len(list(group)) for key, group in groupby(d)]
    return  Dn(counts)
    
    '''
    limit = x
    numberOfDivisors=0

    for i in xrange(1,limit):
        if (x % i == 0):
            limit = x / i
            if (limit != i):
                numberOfDivisors+=1
            numberOfDivisors+=1
    return numberOfDivisors;
'''
def calcNum(l,prm):
    s=1
    for i,pows in enumerate(l):
        s*=prm[i]**pows
    return s

def generateNumber(l,previ,i):
    global prm
    t = l+[0]
    

    
class hcn():
    def __init__(self,n,primfac):
        self.n=n
        self.primfac=primfac
        
N=1000
k=10
u=1000**2
prm = primes2(u)
print 'prime array ready'

hcns =  set(    [1,2,4,6,12,24,36,48,60,120,180,240,360,720,840,
 1260,1680] )

hcnFactors = [[1],[2],[1,1],[2,1],[3,1],[2,2],[4,1],[2,1,1],[3,1,1],[2,2,1],[4,1,1],[3,2,1],[4,2,1],[3,1,1,1],[2,2,1,1]]
factorizations ={}
for i in hcns:
    factorizations[i] = primeFactors(i) 


def smooth():
    global hcns,k,factorizations
    intervals = k
    previ = 0
    degenHcns =set()
    for i in (hcns):
        if i>N: break
        d = [len(list(group)) for key, group in groupby(primeFactors(i))]
        factorizations[i] = d
        #print i,d
        #print previ,i,factorizations[i]
        #need to insert degenerate hcns after previ
        for t in permutations ( factorizations[i]+[0]*2 ):                
            p=t
            newHCN  =  calcNum(t, prm)
            if newHCN<N:
                factorizations[newHCN] = list( p )
                degenHcns.add(newHCN)
    
        previ=i
    hcns=set ( sorted ( hcns.union(degenHcns) ) ) 
    #print (hcns)
for i in range(10):smooth()
hcns = sorted(hcns)
print hcns
for i in hcns:
    print i,Dn(factorizations[i]) ,factorizations[i]
exit(0)
def Mnk(n,k):
    global l
    return max( l[n:n+k] )



def Suk(u,k):
    s=0
    for n in xrange(1,u-k+1+1):
        s+= Mnk(n,k)
    return s
l=[0]*(u+2)
for i in prm: l[i]=2
print 'primes in l'
for i in xrange(u+1):
    if l[i]!=0: 
        l[i]=divisors(i)


print 'divisor array ready'
for k in (500,1000,2000,10000):
    sol=Suk(u,k)
    print 'S(u=%7d , k=%5d)\t=%12d' % (u,k,sol)
        
        
