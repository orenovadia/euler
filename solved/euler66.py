

from math import sqrt

def firstx(D,y):
    lhs = D*y**2
    posx = int (sqrt ((lhs-1.0)/2.0 ))
    for i in range(posx-1,posx+3 ,1):
        #print i
        if (i+1)*(i-1)==lhs:
            #print 'found',i
            return i
    return None

for D in range(2,20):
    for y in range(1,55):
        sol = firstx(D,y)
        if sol: 
            print 'D:',D,'y:',y,'x:',sol
            break