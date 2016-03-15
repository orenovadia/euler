import time
from matplotlib import pyplot
#from eulertools import primes
from fractions import Fraction
from itertools import count as crange
from itertools import groupby

def countVariations(n):
    count = 0
    y = n+1
    for x in xrange(n*2+1,n,-1):
        y=(x-n)/x/n
        while x*y<n*(x+y):
            y+=1
        if x*y==n*(x+y):
            count+=1
    return count



def countVariationsxy(n,goal):
    count = 0
    x=n+1
    start, end = n+1 , n*2+1
    posibility = end-start+1
    for i,x in enumerate( range(start,end)):
        y1,y2 = x*n/(x-n),x*n/(x-n)+1
        if ((x+y1)*n == y1*x ) or((x+y2)*n == y2*x ) : count+=1
        #if posibility -i + count < goal: break
    return count

def VerboseCountVariationsxy(n,goal):
    count = 0
    x=n+1
    start, end = n+1 , n*2+1
    posibility = end-start+1
    for i,x in enumerate( range(start,end)):
        y1,y2 = x*n/(x-n),x*n/(x-n)+1
        if ((x+y1)*n == y1*x ):
            count+=1
            print x,y1
        elif ((x+y2)*n == y2*x ): 
            count+=1
            print x,y2
        else:
            if False: break
        #if posibility -i + count < goal: break
    return count


def fracCount(n,goal):
    nf = Fraction(1,n)
    count = 0
    x=n+1
    start, end = n+1 , n*2+1
    posibility = end-start+1
    for i,x in enumerate( range(start,end)):
        y1,y2 = x*n/(x-n),x*n/(x-n)+1
        xf,y1f,y2f = Fraction(1,x) ,Fraction(1,y1) ,Fraction(1,y2) 
        if (xf+y1f == nf):
            count+=1
            #print xf*2,y1f*2,nf*2
        elif (xf+y2f == nf): 
            count+=1
            #print xf*2,y2f*2,nf*2
        else:
            if False: break
        #if posibility -i + count < goal: break
    return count


def primeFactors(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n //= d
        d += 1
    if n > 1:
        primfac.append(n)
    #return primfac
    return [len(list(group)) for key, group in groupby(primfac)]

def Dn(l):
    return (reduce(lambda x,y: x*(2*y+1) , [1]+l)+1)/2

minimal=10**20
def powerCheck(l,n,goal,itm,dontpass):
    global prm,minimal
    time.sleep(0.001)
    d = Dn(l[:n+1])
    if n==itm: return
    while d<goal and l[n]<dontpass:
        l[n]+=1
        d= Dn(l[:n+1])
        if d>goal:
            #print d , l[:n+1]
            dn = calcNum(l[:n+1],prm)
            if dn< minimal:
                print d,dn ,l[:n+1]
                minimal = dn
        else:
            powerCheck(l,n+1,goal,itm,l[n])
    l[n]=0
        

def calcNum(l,prm):
    s=1
    for i,pow in enumerate(l):
        s*=prm[i]**pow
    return s
goal = 10

prm = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997] 
l=[0]*len(prm)
#primes(goal)
print prm
print l
powerCheck(l, 0, goal,len(l),20)

#print Dn(primeFactors(180180**2))

'''
divisors = [6,4,2,2]
i=172960
d=0
while d<1000:
    d = (Dn(primeFactors(i**2))+1)/2
    print i,'\t',d
    i+=10




grounds = [0,]
i=70
for i in (1,2,3,5,7):
    print i,'\t',2520/i,'\t',countVariationsxy(2520/i,1)
    i*=6
exit(0)
for i in (1,2,3,4,5,6,7,9,10,12,14,15,19,20,21,28,30,35,36,42,45,60,63,70,84,90,105,126,140,180,210,252,315,420,630,1260):
    #print i,fracCount(i,1)
    grounds.append(countVariationsxy(i,1))
    i+=1
print grounds
guess=[]
goal=100

for i in xrange(200,len (grounds)/4):
    a2,a4,a8 = [grounds[i*4],grounds[i*2],grounds[i]]
    print a2,a4,a8
    count = 0
    while a2<goal:
        count+=1
        a2,a4,a8 = a2+a4-a8,a2,a4
    guess.append([i,a2,count])
    print a2,i
for r in guess: print r
        


N=10**5
x=[]
y=[]
nexti = 9200
goal = 1000
maxd = 0
best = 250
print VerboseCountVariationsxy(24,1)
#207280 - 102
#207290 - 99



while maxd<goal:
    for i in range(nexti-3,nexti+3):        
        d = countVariationsxy(i, best)
        if d>maxd:
            print i,d,best,maxd
            maxd=d
            best = i
            nexti=i*2
print maxd,best

i=1
while True:
    i+=1
    d = countVariationsxy(i, 1)
    if d>goal: 
        print i,d
        break

exit(0)
if 1:    
    x.append(i)
    y.append(d)
pyplot.scatter(x,y)
pyplot.show()

'''



