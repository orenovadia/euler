from  math import sqrt,floor
import time
import Queue
def sum_sq_n(N):
    try:z = N**0.5
    except: print N ; raise
    m = int( floor( z ))
    #print z,m , N,(2*m**2+3*m-5)
    return int ( m*(  N - (2*m**2+3*m-5)/6.0   ) )


def sum_n(N):
    return N*(N+1)/2
def create_initial_conditions(l=[1,1,2,1]):
    length = len(l)
    sig_sqrt_n = sum( [ int( floor(c**0.5)) for c in l  ])
    sig = sum (l)
    return length,sig_sqrt_n,sig
def pop_last_n_from_last_list(length,sig_sqrt_n,sig,lasts,n_to_pop):
    assert n_to_pop < len(lasts),n_to_pop
    for i in range(n_to_pop):
        t = lasts.pop(-1)
        sig -= t
        sig_sqrt_n -= int ( t ** 0.5 )
    return length-n_to_pop   ,sig_sqrt_n,sig,lasts

def masger(length,sig_sqrt_n,sig,top):
    high_low = top
    low_high = top
    low_low = top/2
    for i in range(13):
        sig += sum_n( sig_sqrt_n )
        length += sig_sqrt_n
        sig_sqrt_n += sum_sq_n(sig_sqrt_n)
        #print length
        if length > high_low: return 'high'
        if low_low<length<low_high: return 'low'

def is_masger(length,sig_sqrt_n,sig,top,lasts,verbose = False):
    lasts = list(lasts)
    high = masger(length,sig_sqrt_n,sig,top)
    to_pop = len(lasts)*7/8
    length,sig_sqrt_n,sig,lasts=pop_last_n_from_last_list(length,sig_sqrt_n,sig,lasts,to_pop)
    low = masger(length,sig_sqrt_n,sig,top)
    if verbose:
        print length,sig_sqrt_n,sig,len(lasts),high,low
    if high == low:
        return False
    if high == 'high' and low=='low':
        #print 'closed masger',
        return True
    assert False , 'what?'
last_masger_idx = 1
def reduce_a_masger_and_return_the_params(length,sig_sqrt_n,sig,top,lasts):
    ret =  is_masger(length,sig_sqrt_n,sig,top,lasts,verbose = True)
    assert ret
    q = Queue.LifoQueue()
    global last_masger_idx
    print 'doing masger for ',length,sig_sqrt_n,sig,top
    print 'len lasts = ',len(lasts)
    for i in range(last_masger_idx,len(lasts),1):
        q.put(  (length,sig_sqrt_n,sig,list(lasts))  )
        length,sig_sqrt_n,sig,lasts=pop_last_n_from_last_list(length,sig_sqrt_n,sig,lasts,2)
        ret = is_masger(length,sig_sqrt_n,sig,top,lasts)
        if not ret:
            last_masger_idx = i*2
            print 'found minimal masger under',length ,'index = ',i , len(lasts)
            return q.get_nowait()
    return q.get_nowait()
def reduce_a_masger_and_return_the_params_bin_search(length,sig_sqrt_n,sig,top,lasts):
    ret =  is_masger(length,sig_sqrt_n,sig,top,lasts,verbose = True)
    assert ret
    q = Queue.LifoQueue()
    imin , imax = 0 , len(lasts)-1
    while imin<= imax:
        imid = (imin + imax) /2
        q.put(  (length,sig_sqrt_n,sig,list(lasts))  )
        length,sig_sqrt_n,sig,lasts=pop_last_n_from_last_list(length,sig_sqrt_n,sig,lasts,imid)
        ret = is_masger(length,sig_sqrt_n,sig,top,lasts)
        if ret: #reduce size
            imax = imax -1
            length,sig_sqrt_n,sig,lasts = q.get_nowait()
        else:
            imin = imid +1
            length,sig_sqrt_n,sig,lasts = q.get_nowait()
        print imax,imid
    return pop_last_n_from_last_list(length,sig_sqrt_n,sig,lasts,imid-1)


def it_masgerim(length,sig_sqrt_n,sig,top,lasts):
    print 'len lasts in : %s'%len(lasts)
    lasts = lasts[-10000:]
    length,sig_sqrt_n,sig,lasts = reduce_a_masger_and_return_the_params(length,sig_sqrt_n,sig,top,lasts)
    print length,sig_sqrt_n,sig
    sig += sum_n( sig_sqrt_n )
    length += sig_sqrt_n
    lasts = lasts[-50:]
    print 'calcing lasts'
    lasts = make_new_last_list(lasts,sig_sqrt_n)
    sig_sqrt_n += sum_sq_n(sig_sqrt_n)
    print 'advanced to',length,sig_sqrt_n,sig
    if top<=length<=top*1.01:
        print length,sig_sqrt_n,sig
        if top<=length<=top + len(lasts):
            lasts.reverse()
            for i in lasts:
                length-=1
                sig -= i
                if length == top: break
            print length,sig
        return
    else:
        it_masgerim(length,sig_sqrt_n,sig,top,lasts)
    print length
    return 'bla'
    
def start_iteration(l_in=[1,1,2,1],top=10**9):
    length,sig_sqrt_n,sig = create_initial_conditions(l_in)
    l=[]
    lasts=[]
    lasts = l_in[-130:]
    it_masgerim(length,sig_sqrt_n,sig,top,lasts)
def it(l_in=[1,1,2,1],top=10**9):
    length,sig_sqrt_n,sig = create_initial_conditions(l_in)
    l=[]
    lasts=[]
    lasts = l_in[-130:]
    q = Queue.LifoQueue()
    print create_initial_conditions()
    for i in range(1,130000):
        sig += sum_n( sig_sqrt_n )
        length += sig_sqrt_n
        lasts = make_new_last_list(lasts,sig_sqrt_n)
        sig_sqrt_n += sum_sq_n(sig_sqrt_n)
        l.append(length)

        lasts = lasts[-2100:]
        if length > top:
            if length - len(lasts) <= top:
                raise Exception('found it!!!')
            if length - top*3 > top: assert False , 'way overshoot'
            print 'poping',length
            length,sig_sqrt_n,sig,lasts = q.get_nowait()
            try: length,sig_sqrt_n,sig,lasts=pop_last_n_from_last_list(length,sig_sqrt_n,sig,lasts,4)
            except: print 'popped all',q.qsize() , length   ; continue
            q.put(  (length,sig_sqrt_n,sig,lasts)  )
        else:
            q.put(  (length,sig_sqrt_n,sig,lasts)  )
        print length , sig ,sig_sqrt_n#, lasts[-10:]
        
        
    print length , sig ,sig_sqrt_n#, lasts[-10:]
    return l

def make_new_last_list(last_list,N):
    l = []
    last_list.reverse()
    #total_new_n_to_append = sum( [ int(c**0.5) for c in last_list]  )
    #print 'make_new_last_list',total_new_n_to_append , N
    for i in last_list:
        nums_to_append = int( i ** 0.5)
        l.append(i)
        for j in range(nums_to_append):
            l.append(N)
            N-=1
    
    l.reverse()
    return l
import euler535brute
l = euler535brute.f( 7415 )
start_iteration (l,top=10**18)
exit()
for i in range ( 1,len(l)):
    print i,
    try:
        print  start_iteration (l[:i],top=10**9)
        break
    except: continue
