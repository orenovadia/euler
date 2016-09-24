from Queue import Queue

l = []
with open('p081_matrix.txt', 'rb') as f:
    for row in f:
        l.append(map(int, row.split(',')))

dist = {}
prev = {}
weight = {}
dim = len(l)
Q = list()
print dim
for i in range(dim):
    for j in range(dim):
        dist[i, j], prev[i, j] = None, None
        weight[i, j] = l[i][j]
        Q.append((i, j))

dist[0, 0] = weight[0, 0]


def getMinDist(Q):
    global dist, prev
    minimalVert = Q[0]
    minDist = dist[minimalVert]

    for v in Q[1:]:
        if dist[v]:
            if dist[v] < minDist:
                minimalVert = v
                minDist = dist[minimalVert]
    Q.remove(minimalVert)
    return minimalVert


def neighbors(v, Q, dim):
    ret = []
    i, j = v
    # ret.append((i-1,j))
    ret.append((i + 1, j))
    # ret.append((i,j-1))
    ret.append((i, j + 1))
    for u in [(i + 1, j), (i, j + 1)]:  #(i - 1, j), (i, j - 1)
        x, y = u
        if 0 > x or dim <= x:
            ret.remove(u)
            continue
        if 0 > y or y >= dim:
            ret.remove(u)
            continue
        if u not in Q:
            ret.remove(u)
    return ret


while Q:
    u = getMinDist(Q)
    # print u, neighbors(u, Q, dim)
    for v in neighbors(u, Q, dim):
        if dist[v] == None:
            dist[v] = dist[u] + weight[v]
        else:
            try:
                alt = dist[u] + weight[v]
                dist[v] = min(alt, dist[v])
            except:
                print 'ex'
print 'end is at', dist[(dim - 1, dim - 1)]
