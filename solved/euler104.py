from math import log10

def getFibonnacciNumber(n):
    from itertools import count as crange
    prev , this = 0 , 1
    for i in crange(n-1):
        prev , this = this , prev+this
    return this

def yieldFibonnacciNumber(n,startFrom = 0):
    from itertools import count as crange
    prev , this = 0 , 1
    for i in crange(n-1):
        prev , this = this , prev+this
        if i>=startFrom-1: yield this


alldigits=set()
alldigits = [int (x) for x in range(1,10)]

def checkPandigitMS(n):
    global alldigits
    n /= 10 ** (  int(log10(n) + 1)  - 9 )
    l = set (int (x) for x  in  str(n) )
    if len ( l.intersection(alldigits) ) < 9: return False
    return True

def checkPandigitLS(n):
    global alldigits
    n %= 1000000000
    l = set (int (x) for x  in  str(n) )
    if len ( l.intersection(alldigits) ) < 9: return False
    return True

sf=0
#492982
#print checkPandigitLS( getFibonnacciNumber(492982))

for k,i in enumerate ( yieldFibonnacciNumber(10**12,startFrom=sf) ) :
    if checkPandigitLS( i):
        print 'LS: ' ,'\t', k+sf+2
        if checkPandigitMS ( i ):
            print 'MS: ' ,'\t', k+sf+2
            break
