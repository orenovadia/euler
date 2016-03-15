from numpy import place

maxPath=0

def calcWay(tree,s,level,place,depthToGo):
    global maxPath
    if level == depthToGo: return
    s+= tree[level][place]
    if s>=maxPath: maxPath=s
    calcWay(tree,s,level+1,place+1,depthToGo)
    calcWay(tree,s,level+1,place,depthToGo)

def relaxation(tree,level,place):
    if level ==len(tree)-1: return
    tree[level][place]+= max(tree[level+1][place], tree[level+1][place+1]   )

tree = []
treeFile = 'p067_triangle.txt'
#treeFile = 'tree_euler18.txt'

with open(treeFile ,'rb') as f:
    #[tree.append(x) for map(int , r.split()) for r in f.read().split('')]
    for row in f:
        tree.append( [ int(x) for x in row.split() ] )
        
print 'Tree has # lines: ',len( tree ) 

#calcWay(tree,0,0,0,len(tree))
print maxPath

for i in range (len(tree)-1,-1,-1):
    
    for x,l in enumerate ( tree[i]): relaxation(tree, i, x)
    print tree[i]
print tree[0][0]
