from eulertools import Dn,primeFactors,primesFromMtoN
from itertools import groupby,combinations
from math import log,sqrt,factorial
from time import time as thistime
from bisect import bisect,bisect_right,bisect_left

st = thistime()

N=10**6
minimal = N
'''from eulertools import primes
prm = primes(N/6)
print prm 
exit(0)
'''
filename = 'primes%d.txt' % (int(sqrt(N))*10)
#prm =[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163]
with open (filename,'rb') as f:
    prm = eval(f.read())
#print prm
nPrm = len(prm)
maxPrime = prm[-1]
pgTestPrimes=prm[:bisect(prm,sqrt(N))]
#print pgTestPrimes

x_vec=list([1])
x_vec.append(maxPrime)
pi_vec=set([0])
pi_vec.add(nPrm)
pi_len = len(pi_vec)
pi_func={}
pi_func[1]=0
pi_func[maxPrime]=nPrm

print 'max Prime:' ,maxPrime
print 'num of Primes:' ,nPrm
def pi(x):
    global prm,nPrm,N,maxPrime,x_vec,pi_vec,pi_len,pi_func
    if x<=maxPrime:
        return bisect(prm, x)
    else:
        bis = bisect_left(x_vec, x)
        if bis<pi_len and x_vec[bis]==x:
            print '\n1,x_vec[bis],x,bis,pi_len',1,x_vec[bis],x,bis,pi_len
            return pi_func[x_vec[bis]]
        else:
            xx=x_vec[bis-1]
            xright =1
            if bis<pi_len:
                xright=x_vec[bis]
            print xright,xx,x,N/x
            if abs(xright-x)<abs(xx-x):
                p = pi_func[xright] - primesFromMtoN(x+1,xright,prm)
                print 'from left',p,x,xright
            else:
                p = pi_func[xx] + primesFromMtoN(xx+1,x,prm)
        x_vec[bis:bis] = [x]
        #pi_vec[bis:bis] = [p]
        pi_func[x]=p
        pi_len=len(x_vec)
        return p
    
def writePix(pix):
    global x_vec,pi_vec,pi_func
    #for i in range(len( x_vec)):
    #    pix.write('%d=%d\n' % (x_vec[i] ,pi_func[x_vec[i]] )  )
    for i in sorted(set(x_vec)):
        pix.write('%d=%d\n' % (i ,pi_func[i] )  )
    
def loadPix():
    global x_vec,pi_vec,pi_len,pi_func
    with open('pix.txt','rb') as pix:
        for row in pix:
            x,p = row.split('=')
            x_vec.append(int(x))
            pi_vec.add(int(p.strip()))
            pi_func[int(x)]=int(p.strip())
    x_vec = sorted(x_vec)
    pi_vec = sorted(pi_vec)
    pi_len = len(pi_vec)
    


   
def count7s(n):
    return pi(n**(1.0/7)   )

def counta3bs(n,plist):
    s=0
    for p in prm[:bisect_left(prm, n**(1.0/3)+1)]:
        k = n/(p**3)
        pp=pi(k)
        s+=pp
        #print p,p**3,k,pp,n
        if k>p: s-=1
    return s


def countabc(n,plist):
    s=0
    sqrtn=n**(1.0/2)
    for a in prm[:bisect_left(prm, n**(1.0/2)+1)]:
        for b in prm[bisect_right(prm, a):]:
            print a,b
            c = n/(a*b)
            if c<b: break
            pp=pi(c)
            s+=pp-pi(b)
            print a,b,c,pp,n
    return s

def run():
    global s,N
    print x_vec
    print pi_vec
    s=0
    loadPix()
    
    with open('pix.txt','wb') as pix:
        #try:
            #print pi(1000000),pi(990990)
            #print prm
        print 'N:',N
        s+=count7s(N)
        print '7s:',s
        s+=counta3bs(N, prm)
        print 'counta3bs:',s
        s+=countabc(N, prm)
        print 'countabc:',s
        '''   
        except Exception as err:
            print err
        finally:'''
        writePix(pix)
        print 'time: ',thistime()-st,'secs'

if __name__ == '__main__':
    run()