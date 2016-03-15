
maxPath=0

def calcWay(tree,s,level,place):
    global maxPath
    if level == len(tree): return
    s+= tree[level][place]
    if s>=maxPath: maxPath=s
    calcWay(tree,s,level+1,place+1)
    calcWay(tree,s,level+1,place)

tree = []
treeFile = 'p067_triangle.txt'
treeFile = 'tree_euler18.txt'

with open('tree_euler18.txt','rb') as f:
    for row in f:
        tree.append( [ int(x) for x in row.split() ] )
        
print 'Tree has # lines: ',len( tree ) 

calcWay(tree,0,0,0)
print maxPath