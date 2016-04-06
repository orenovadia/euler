import timeit
def M(n):
    return max([i for i in xrange(n) if i==(i**2)%n] )

for i in range(1,20):
    print i,M(i)#timeit.timeit('M(i)',setup="from __main__ import M,i",number=1)