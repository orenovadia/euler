l=[1, 1, 2, 1, 3, 2, 4, 1, ]
lower_ind,upper_ind,last_circled = 3,7,4
import sys
N=100
try: N=int(sys.argv[1])
except:pass
def f(N):
    global l , lower_ind , upper_ind , last_circled
    l=[1, 1, 2, 1, 3, 2, 4, 1, ]
    lower_ind,upper_ind,last_circled = 3,7,4
    while (len(l)<N):
        n_to_add = l[lower_ind+1]
        circles_to_add = int(n_to_add**0.5)
        for j in range(circles_to_add):
            last_circled+=1
            l.append(last_circled)
        l.append(n_to_add)
        lower_ind+=1
    #print len(l[:N]),sum(l[:N]),l[N-15:N]
    return l[:N]
digsqrt = lambda x: int(x**0.5)
def seqgen():
    yield 1
    cnt=1
    for k in seqgen():
        rs = digsqrt(k)
        for j in range(rs):
            if cnt>1:
                yield cnt
            cnt+=1
        yield k

for i,j in enumerate(seqgen()):
    print j,
    if i>100: break

if __name__ == '__main__':
    #ret = f(N)
    #print len(ret) , sum(ret)
    print