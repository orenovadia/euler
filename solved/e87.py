from time import sleep

from euler.eulertools import primes

# N = 50
N = 50000000
n_1_4 = int(N ** 0.25) + 1
n_1_3 = int(N ** (1.0 / 3.0)) + 1
n_1_2 = int(N ** 0.5) + 1
p = primes(n_1_2 + 100)
len_p = len(p)
print 'n_1_2',n_1_2
print 'n_1_3',n_1_3
print 'n_1_4',n_1_4
print 'number of primes up to sqrt(n)', len_p
c = 0
s=set()
for l in p:
    ll = l ** 2
    # if l > n_1_2:
    #     break
    for n in p:
        nn = n ** 3
        # if n > n_1_3:
        #     break
        # if ll+nn>N:
        #     break
        for m in p:
            # if m > n_1_4:
            #     break
            # print l,n,m,ll + nn + m ** 4
            if ll + nn + m ** 4 <= N:
                s.add(ll + nn + m ** 4)
                c += 1
            else:
                break
print c
print len(s)