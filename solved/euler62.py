'''
Created on Feb 26, 2015

@author: oovadia
'''
 
def arePermutations(a,b):
    la =  sorted(str(a))
    lb = sorted(str(b))
    for ia ,ib in zip(la,lb):
        if ia != ib: return False
    return True
         
    

print arePermutations(345**3, 384**3)
goal = 5
digits=12
l=[]
for i in xrange(100000000):
    i3=i**3
    if len(str(i3))==digits:
        #print i,i3
        l.append(i3)
    elif len( str(i3) )>digits: break
print l
iset=set()
ilist =[]
jset=set()


for i,li in enumerate(l):
    perms=1
    for j in range(i+1,len(l)):
        if arePermutations(l[i], l[j]):
            perms+=1
            if perms==goal:
                print perms, l[i]
                exit(0)
            iset.add(l[i])
            jset.add(l[j])
            ilist.append(l[i])
            print l[i],l[j]
