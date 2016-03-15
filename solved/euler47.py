from itertools import count
m=[]
with open ('345in.txt','rb') as f:
    for row in f:
        m.append( [int(x) for x in row.strip().split() ]) 

N = len(m)
for i in range(N):
    m[i] = sorted(m[i])

for row in m:
    print row