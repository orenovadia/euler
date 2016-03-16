from  numpy import sqrt, floor
import time


def sum_sq_n(N):
    try:
        z = N ** 0.5
    except:
        print N; raise
    m = int(floor(z))
    # print z,m , N,(2*m**2+3*m-5)
    return int(m * (N - (2 * m ** 2 + 3 * m - 5) / 6.0))


def sum_n(N):
    return N * (N + 1) / 2


def create_initial_conditions(l=[1, 1, 2, 1]):
    length = len(l)
    sig_sqrt_n = sum([int(floor(c ** 0.5)) for c in l])
    sig = sum(l)
    return length, sig_sqrt_n, sig


def it(l_in=[1, 1, 2, 1], top=200):
    length, sig_sqrt_n, sig = create_initial_conditions(l_in)
    l = []
    lasts = []
    lasts = l_in[-1:]
    print create_initial_conditions(l_in)
    for i in range(13):
        sig += sum_n(sig_sqrt_n)
        length += sig_sqrt_n
        lasts = make_new_last_list(lasts, sig_sqrt_n)
        sig_sqrt_n += sum_sq_n(sig_sqrt_n)
        l.append(length)
        # print sig
        # print sig_sqrt_n
        # print '****************'
        lasts = lasts[-10:]
        if length > top: break
        print length, sig, sig_sqrt_n, lasts[-10:]
    return l


def make_new_last_list(last_list, N):
    l = []
    last_list.reverse()
    total_new_n_to_append = sum([int(c ** 0.5) for c in last_list])
    # print 'make_new_last_list',total_new_n_to_append , N
    for i in last_list:
        nums_to_append = int(i ** 0.5)
        l.append(i)
        for j in range(nums_to_append):
            l.append(N)
            N -= 1

    l.reverse()
    return l


def old_make_new_last_list(last_list, N):
    l = []
    total_new_n_to_append = sum([int(c ** 0.5) for c in last_list])
    N -= total_new_n_to_append - 1
    for i in last_list:
        nums_to_append = int(i ** 0.5)
        for j in range(nums_to_append):
            l.append(N)
            N += 1
        l.append(i)
    return l


def recur(sig, sig_sqrt_n, length, lasts, l, target):
    len_lasts = len(lasts)
    print length, len_lasts, sig
    if length - len_lasts <= target <= length:  #
        print sig, sig_sqrt_n, length, target
        for i in range(length - target):
            length -= 1
            sig -= lasts.pop(-1)
            print length, sig
        print length, sig
        exit(0)
    elif length < target:
        sig += sum_n(sig_sqrt_n)
        length += sig_sqrt_n
        lasts = make_new_last_list(lasts, sig_sqrt_n)
        sig_sqrt_n += sum_sq_n(sig_sqrt_n)
        l.append(length)
        ret = recur(sig, sig_sqrt_n, length, list(lasts), l, target)
        while ret == 'too_far':
            try:
                last_to_sub = lasts.pop(-1)
                print 'popping', last_to_sub,
                len_lasts = len(lasts)
            except:
                print 'EMPTY', length, l
                l.pop(-1)
                return 'too_far'
            sig -= last_to_sub
            sig_sqrt_n -= int(last_to_sub ** 0.5)
            length -= 1
            ret = recur(sig, sig_sqrt_n, length, list(lasts), l, target)
        if length > target:
            # raise Exception('skipped over')
            l.pop(-1)
            print length, len_lasts, '*',
            return 'too_far'
    elif length > target:
        return 'too_far'


def start_recurr(l_in=[1, ]):
    length, sig_sqrt_n, sig = create_initial_conditions(l_in)
    lasts = l_in[-1:]
    target = 10 ** 3
    print recur(sig, sig_sqrt_n, length, lasts, [], target)


# start_recurr()
import Queue


def it_with_lasts(l_in=[1, 1, 2, 1]):
    length, sig_sqrt_n, sig = create_initial_conditions(l_in)
    lasts = l_in[-1:]
    target = 10 ** 3
    l = []
    q = Queue.LifoQueue()
    for i in range(13000):
        if length - len(lasts) <= target <= length:
            print 'FOUND'
            print length, sig
            exit(0)
        elif length > target:
            print 'subing',
            try:
                last_to_sub = lasts.pop(-1)
                sig -= last_to_sub
                sig_sqrt_n -= int(last_to_sub ** 0.5)
                length -= 1

                continue
            except:
                print 'EMPTY\n'
                sig, sig_sqrt_n, length, lasts, l, target = q.get_nowait()
        params = (sig, sig_sqrt_n, length, lasts, l, target)
        q.put(params)
        sig += sum_n(sig_sqrt_n)
        length += sig_sqrt_n
        lasts = make_new_last_list(lasts, sig_sqrt_n)
        sig_sqrt_n += sum_sq_n(sig_sqrt_n)
        l.append(length)
        # print sig
        # print sig_sqrt_n
        print '*************'
        lasts = lasts[-1000:]
        print lasts[-10:]
        print l, sig
        if length > target: break
    print l
    print len(lasts)
    return l


# print it()
it()
# it()
# print create_initial_conditions()

'''
    
    orens-MacBook-Air:Desktop orenovad$ time pypy euler535.py
    498677663473543476 86 1000001138
    
    real	29m8.931s
    user	0m40.939s
    sys	3m59.144s

    
'''
