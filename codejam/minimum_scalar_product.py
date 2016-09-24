def read_3_lines_give_two_lists(f):
    f.readline()
    l1 = f.readline().split()
    l2 = f.readline().split()
    return map(int,l1),map(int,l2)
def dot(x,y):
    return sum(a*b for a,b in zip(x,y))
with open('input.raw','rb') as f, open('out.txt','wb') as of:
    l = int(f.readline())
    for i in xrange(l):
        x,y =  read_3_lines_give_two_lists(f)
        x.sort()
        y.sort(reverse=True)
        print 'Case #%d: %d'%(i+1,dot(x,y))
        of.write('Case #%d: %d\n'%(i+1,dot(x,y)))