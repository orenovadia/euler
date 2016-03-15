from math import log

N=1000
tt=N
minimal = N

""" Input n>=6, Returns a list of primes, 2 <= p < n """
n=N
n, correction = n-n%6+6, 2-(n%6>1)
sieve = [True] * (n/3)
for i in xrange(1,int(n**0.5)/3+1):
    if sieve[i]:
        k=3*i+1|1
        sieve[      k*k/3      ::2*k] = [False] * ((n/6-k*k/6-1)/k+1)
        sieve[k*(k-2*(i&1)+4)/3::2*k] = [False] * ((n/6-k*(k-2*(i&1)+4)/6-1)/k+1)
prm print len (l)= [2,3] + [3*i+1|1 for i in xrange(1,n/3-correction) if sieve[i]]


l = range(1,N+1)
print len (l)
for pn in prm:
    l.remove(pn)
print len (l)
for powa in xrange(2,int ( log(N,2) ) +1 ):
    i=2
    d = i**powa
    while d<=N:
        try: l.remove(d)
        except:pass
        i+=1
        d = i**powa
print len (l)
