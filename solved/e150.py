

tree = []
treeFile = 'tri150.txt'
#treeFile = 'tree_euler18.txt'
treePrev=[]
treeNext=[]
treeIntersect=[]
with open(treeFile ,'rb') as f:
    #[tree.append(x) for map(int , r.split()) for r in f.read().split('')]
    for row in f:
        tree.append( [ int(x) for x in row.split() ] )
        treePrev.append( [ int(x) for x in row.split() ] )
        treeNext.append( [ 0 for x in row.split() ] )
        treeIntersect.append( [ 0 for x in row.split() ] )

        
print 'Tree has # lines: ',len( tree ) ,len(treeIntersect)
ltree = len( tree )
treeIntersect.append( [ 0 for x in range(ltree+1) ] )
mins=10
'''print tree
print treeNext
print treeIntersect
print treePrev'''
def relaxation(tree,level,place):
    global ltree
    if level <ltree-1: 
        tree[level][place]+= (tree[level+1][place]+ tree[level+1][place+1]   )
    return tree[level][place]

#print tree

for i in range (ltree-1,0,-1): #i is how deep we go
    for n in xrange(0,i):
        for k in xrange(n+1):
            level , place = n,k
            #print i,n,k
            t=treeIntersect[level+2][place+1]
            p = tree[level][place] +treePrev[level+1][place]+ treePrev[level+1][place+1] - t
            treeNext[level][place] =p
            if p<mins:
                mins=p 
                print 'new min: ',mins,'at: ',n,k,'i=',i
    treeIntersect,treePrev,treeNext = treePrev,treeNext,treeIntersect
   
#for row in treeNext: print row
'''for i in range (0,ltree): #i is how deep we go
    for n in xrange(i,-1,-1):
        for k in xrange(n+1):
            print i,n,k
            t = relaxation(tree, n, k) 
            if t < mins:
                mins=t 
                

'''
#    for x,l in enumerate ( tree[i]): relaxation(tree, i, x)
#    print tree[i]
#print tree[0][0]


'''t=0
two19=2**19
two20=two19*2
n=1
nele=0
with open('tri150.txt','wb') as f:
    for k in xrange(1,500500):
        t=(615949*t+797807)%two20
        s=t-two19
        if nele ==n:
            f.write('\n')
            n+=1
            nele=0
        f.write ( str(s)+' ' )
        #print k,s
        nele+=1
'''
