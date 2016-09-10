import ctypes
from bisect import bisect
from math import sqrt, factorial
from random import randint

# gcc -Wall -Wextra -O -ansi -pedantic -shared euler_c.c -o euler_c.so
load_c_lib = False
if load_c_lib:
    c = ctypes.cdll.LoadLibrary('./euler_c.so')
    square_sum_of_digits = c.square_sum_of_digits
    c_sum_of_digits = c.sum_of_digits

def sum_of_digits(n):
    return sum(int(i) for i in str(n))


def divisorGenerator(n_n):
    large_divisors = []
    small_divisors = []
    for i in xrange(1, int(sqrt(n_n) + 1)):
        if n_n % i is 0:
            small_divisors.append(i)
            if i is not n_n / i:
                large_divisors.insert(0, n_n / i)
    return small_divisors + large_divisors


def Dnsquare(l):
    return (reduce(lambda x, y: x * (2 * y + 1), [1] + l) + 1) / 2


def Dn(l):
    return reduce(lambda x, y: x * (y + 1), [1] + l)


def totient(p1, p2):
    return (p1 - 1) * (p2 - 1)


def arePermutations(a, b):
    la = sorted(str(a))
    lb = sorted(str(b))
    for ia, ib in zip(la, lb):
        if ia != ib: return False
    return len(la) == len(lb)


def sigma0(n_n):
    from itertools import groupby
    prm = primeFactors(n_n)
    counts = [len(list(group)) for key, group in groupby(prm)]
    return Dn(counts)


def sigmakOfN2(k, n_n):
    from itertools import groupby
    prm = primeFactors(n_n)
    counts = [len(list(group)) for key, group in groupby(prm)]
    prm = list(set(prm))
    s = 1
    for i, _pow in enumerate(counts):
        p = prm[i]
        s *= (p ** ((_pow + 1) * k) - 1) / (p ** k - 1)
    return s


def primes(N):
    from numpy import where
    alls = [True] * (N + 1)
    for i in xrange(2, int(sqrt(N)) + 1):
        if alls[i]:
            for j in xrange(N):
                m = i ** 2 + i * j
                if m > N: break
                alls[m] = False
    alls[0], alls[1] = [False] * 2
    primes = where(alls)[0]
    numP = len(primes)
    print 'Number o primes', numP
    return list(primes)


def primes2(n_n):
    """ Input n_n>=6, Returns a list of primes, 2 <= p < n_n """
    n_n, correction = n_n - n_n % 6 + 6, 2 - (n_n % 6 > 1)
    sieve = [True] * (n_n / 3)
    for i in xrange(1, int(n_n ** 0.5) / 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[k * k / 3::2 * k] = [False] * ((n_n / 6 - k * k / 6 - 1) / k + 1)
            sieve[k * (k - 2 * (i & 1) + 4) / 3::2 * k] = [False] * (
                (n_n / 6 - k * (k - 2 * (i & 1) + 4) / 6 - 1) / k + 1)
    return [2, 3] + [3 * i + 1 | 1 for i in xrange(1, n_n / 3 - correction) if sieve[i]]


def primesFromMtoN(M, N, prmCheck):
    lim = N
    """ Get an upper limit from the user to determine the generator's termination point. """
    sqrtlim = sqrt(float(lim))
    """ Get the square root of the upper limit. This will be the upper limit of the test prime array 
    for primes used to verify the primacy of any potential primes up to (lim). Primes greater than 
    (sqrtlim) will be placed in an array for extended primes, (xp), not needed for the verification 
    test. The use of an extended primes array is technically unnecessary, but helps to clarify that we 
    have minimized the size of the test prime array. """
    pp = M
    tp = prmCheck[:bisect(prmCheck, int(sqrtlim))]  # test primes
    size = N - M + 1
    sieve = [True] * size #no sograim
    i = 0
    for i in xrange(size):
        k = i + M
        if sieve[i]:
            for tpc in tp:
                if k % tpc == 0:
                    tp.remove(tpc)
                    sieve[i] = False
                    i += tpc
                    while i < size:
                        sieve[i] = False
                        i += tpc
                    break
    c = 0
    for i in sieve:
        if i: c += 1
    return c


def pGSimple(N):
    pp = 2
    ps = [pp, ]

    while pp < N:
        pp += 1
        for a in ps:
            if pp % a == 0:
                break
        else:
            ps.append(pp)
    print 'Number o primes', len(ps)
    return ps


def factorialcomponents(n_n):
    i = 1
    if n_n == 1:
        print 1, '* 1!'
        return
    if n_n == 0: return
    while factorial(i) < n_n: i += 1
    fac = factorial(i - 1)
    print n_n / fac, '*', i - 1, '!'
    factorialcomponents(n_n - n_n / fac * fac)


def getFibonnacciNumber(n_n):
    from itertools import count as crange
    prev, this = 0, 1
    for i in crange(n_n - 1):
        prev, this = this, prev + this
    return this


def yieldFibonnacciNumber(n_n, startFrom=0):
    from itertools import count as crange
    prev, this = 0, 1
    for i in crange(n_n - 1):
        prev, this = this, prev + this
        if i >= startFrom - 1: yield this


def isFermetPrime(p):
    for j in xrange(5):
        a = randint(1, p - 1)
        if pow(a, p - 1, p) != 1: return False
    return True


def primeFactors(n_n):
    # from itertools import groupby
    primfac = []
    d = 2
    while d * d <= n_n:
        while (n_n % d) == 0:
            primfac.append(d)  # supposing you want multiple factors repeated
            n_n //= d
        d += 1
    if n_n > 1:
        primfac.append(n_n)
    return primfac
    # counts = [len(list(group)) for key, group in groupby(factors)]


def PG78(N):
    lim = N
    """ Get an upper limit from the user to determine the generator's termination point. """
    sqrtlim = sqrt(float(lim))
    """ Get the square root of the upper limit. This will be the upper limit of the test prime array 
    for primes used to verify the primacy of any potential primes up to (lim). Primes greater than 
    (sqrtlim) will be placed in an array for extended primes, (xp), not needed for the verification 
    test. The use of an extended primes array is technically unnecessary, but helps to clarify that we 
    have minimized the size of the test prime array. """
    pp = 2
    """ Initialize the variable for the potential prime, setting it to begin with the first prime 
    number, (2). """
    ss = [pp]
    """ Initialize the array for the skip set, setting it at a single member, being (pp=2). Although 
    the value of the quantity of members in the skip set is never needed in the program, it may be 
    useful to understand that future skip sets will contain more than one member, the quantity of which 
    can be calculated, and is the quantity of members of the previous skip set multiplied by one less 
    than the value of the prime which the new skip set will exclude multiples of. Example - the skip 
    set which eliminates multiples of primes up through 3 will have (3-1)*1=2 members, since the 
    previous skip set had 1 member. The skip set which eliminates multiples of primes up through 5 will 
    have (5-1)*2=8 members, since the previous skip set had 2 members, etc. """
    ep = [pp]
    """ Initialize the array for primes which the skip set eliminate multiples of, setting the first 
    member as (pp=2) since the first skip set will eliminate multiples of 2 as potential primes. """
    pp += 1
    """ Advance to the first potential prime, which is 3. """
    rss = [ss[0]]
    """ Initialize an array for the ranges of each skip set, setting the first member to be the range 
    of the first skip set, which is (ss[0]=2). Future skip sets will have ranges which can be 
    calculated, and are the sum of the members of the skip set. Another method of calculating the range 
    will also be shown below. """
    tp = [pp]
    """ Initialize an array for primes which are needed to verify potential primes against, setting the 
    first member as (pp=3), since we do not yet have a skip set that excludes multiples of 3. Also note 
    that 3 is a verified prime, without testing, since there are no primes less than the square root of 
    3. """
    i = 0
    """ Initialize a variable for keeping track of which skip set range is current. """
    rss.append(rss[i] * tp[0])
    """ Add a member to the array of skip set ranges, the value being the value of the previous skip 
    set range, (rss[0]=2), multiplied by the value of the largest prime which the new skip set will 
    exclude multiples of, (tp[0]=3), so 2*3=6. This value is needed to define when to begin 
    constructing the next skip set. """
    xp = []
    """ Initialize an array for extended primes which are larger than the square root of the user 
    defined limit (lim) and not needed to verify potential primes against, leaving it empty for now. 
    Again, the use of an extended primes array is technically unnecessary, but helps to clarify that we 
    have minimized the size of the test prime array. """
    pp += ss[0]
    """ Advance to the next potential prime, which is the previous potential prime, (pp=3), plus the 
    value of the next member of the skip set, which has only one member at this time and whose value is 
    (ss[0]=2), so 3+2=5. """
    npp = pp
    """ Initialize a variable for the next potential prime, setting its value as (pp=5). """
    tp.append(npp)
    """ Add a member to the array of test primes, the member being the most recently identified prime, 
    (npp=5). Note that 5 is a verified prime without testing, since there are no TEST primes less than 
    the square root of 5. """
    while npp < int(lim):
        """ Loop until the user defined upper limit is reached. """
        i += 1
        """ Increment the skip set range identifier. """
        while npp < rss[i] + 1:
            for n_n in ss:

                npp = pp + n_n
                """ Assign the next potential prime the value of the potential prime plus 
                 the value of the current member of the skip set. """
                if npp > int(lim): break
                """ If the next potential prime is greater than the user defined limit, 
                 then end the 'for n_n' loop. """
                if npp <= rss[i] + 1: pp = npp
                """ If the next potential prime is still within the range of the next skip 
                 set, then assign the potential prime variable the value of the next 
                potential prime. Otherwise, the potential prime variable is not changed 
                 and the current value remains the starting point for constructing the next 
                 skip set. """
                sqrtnpp = sqrt(npp)
                """ Get the square root of the next potential prime, which will be the 
                limit for the verification process. """
                test = True
                """ Set the verification flag to True. """
                for q in tp:
                    if sqrtnpp < q:
                        break
                    elif npp % q == 0:
                        test = False
                        """ Then set the verification flag to False since the next 
                        potential prime is not a prime number. """
                        break
                        """ And end testing through the 'for q' loop. """
                    """ Otherwise, continue testing through the 'for q' loop. """
                if test:
                    if npp <= sqrtlim:
                        tp.append(npp)
                    else:
                        xp.append(npp)
                    """ Otherwise, add it to the array of primes not needed to verify 
                     potential primes against. """
                """ Then continue through the 'for n_n' loop. """
            if npp > int(lim): break
            """ If the next potential prime is greater than the user defined limit, then end 
             the 'while npp<rss[i]+1' loop. """
            """ Otherwise, continue the 'while npp<rss[i]+1' loop. """
        if npp > int(lim): break
        """ If the next potential prime is greater than the user defined limit, then end the 'while 
         npp<int(lim)' loop. """
        """ At this point, the range of the next skip set has been reached, so we may begin
        constructing a new skip set which will exclude multiples of primes up through the value of 
        the first member of the test prime set, (tp[0]), from being selected as potential 
        primes. """
        lrpp = pp
        """ Initialize a variable for the last relevant potential prime and set its value to the 
         value of the potential prime. """
        nss = []
        """ Initialize an array for the next skip set, leaving it empty for now. """
        while pp < (rss[i] + 1) * 2 - 1:
            for n_n in ss:
                npp = pp + n_n
                """ Assign the next potential prime the value of the potential prime plus 
                 the value of the current member of the skip set. """
                if npp > int(lim): break
                """ If the next potential prime is greater than the user defined limit, 
                 then end the 'for n_n' loop. """
                sqrtnpp = sqrt(npp)
                """ Get the square root of the next potential prime, which will be the 
                limit for the verification process. """
                test = True
                """ Set the verification flag to True. """
                for q in tp:
                    if sqrtnpp < q:
                        break
                    elif npp % q == 0:
                        test = False
                        """ Then set the verification flag to False since the next 
                         potential prime is not a prime number. """
                        break
                        """ And end testing through the 'for q' loop. """
                    """ Otherwise, continue testing through the 'for q' loop. """
                if test:
                    if npp <= sqrtlim:
                        tp.append(npp)
                    else:
                        xp.append(npp)
                    """ Otherwise, add it to the array of primes not needed to verify 
                     potential primes against. """
                if npp % tp[0] != 0:
                    nss.append(npp - lrpp)
                    """ Add a member to the next skip set, the value of which is the 
                     difference between the last relevant potential prime and the next 
                     potential prime. """
                    lrpp = npp
                    """ Assign the variable for the last relevant potential prime the 
                     value of the next potential prime. """
                pp = npp
                """ Assign the variable for the potential prime the value of the next 
                 potential prime. """
                """ Then continue through the 'for n_n' loop. """
            if npp > int(lim): break
            """ If the next potential prime is greater than the user defined limit, then end 
             the 'while npp<(rss[i]+1)*2-1' loop. """
            """ Otherwise, continue the 'while npp<(rss[i]+1)*2-1' loop. """
        if npp > int(lim): break
        """ If the next potential prime is greater than the user defined limit, then end the 'while 
         npp<int(lim)' loop. """
        ss = nss
        """ Assign the skip set array the value of the new skip set array. """
        ep.append(tp[0])
        """ Add a new member to the excluded primes array, since the newly constructed skip set 
         will exclude all multiples of primes through the first member of the test prime array. """
        del tp[0]
        """ Delete the first member from the test prime array since future potential primes will 
         not have to be tested against this prime. """
        rss.append(rss[i] * tp[0])
        """ Add a member to the skip set range array with the value of the range of the next skip 
         set. """
        npp = lrpp
        """ Assign the next potential prime the value of the last relevant potential prime. """
        """ Then continue through the 'while npp<int(lim)' loop. """
    """ At this point the user defined upper limit has been reached and the generator has completed 
    finding all of the prime numbers up to the user defined limit. """
    ep.reverse()
    """ Flip the array of excluded primes. """
    [tp.insert(0, a) for a in ep]
    """ Add each member of the flipped array into the beginning of the test primes array. """
    tp.reverse()
    """ Flip the array of test primes. """
    [xp.insert(0, a) for a in tp]
    """ Add each member of the flipped array into the beginning of the extended primes array. """
    return xp


""" Send the completed array of all primes up to the user defined limit back to the function call. """


def PG78toFile(N):
    with open('pgPrimes.txt', 'wb') as f:
        lim = N
        """ Get an upper limit from the user to determine the generator's termination point. """
        sqrtlim = sqrt(float(lim))
        """ Get the square root of the upper limit. This will be the upper limit of the test prime array 
        for primes used to verify the primacy of any potential primes up to (lim). Primes greater than 
        (sqrtlim) will be placed in an array for extended primes, (xp), not needed for the verification 
        test. The use of an extended primes array is technically unnecessary, but helps to clarify that we 
        have minimized the size of the test prime array. """
        pp = 2
        """ Initialize the variable for the potential prime, setting it to begin with the first prime 
        number, (2). """
        ss = [pp]
        """ Initialize the array for the skip set, setting it at a single member, being (pp=2). Although 
        the value of the quantity of members in the skip set is never needed in the program, it may be 
        useful to understand that future skip sets will contain more than one member, the quantity of which 
        can be calculated, and is the quantity of members of the previous skip set multiplied by one less 
        than the value of the prime which the new skip set will exclude multiples of. Example - the skip 
        set which eliminates multiples of primes up through 3 will have (3-1)*1=2 members, since the 
        previous skip set had 1 member. The skip set which eliminates multiples of primes up through 5 will 
        have (5-1)*2=8 members, since the previous skip set had 2 members, etc. """
        ep = [pp]
        """ Initialize the array for primes which the skip set eliminate multiples of, setting the first 
        member as (pp=2) since the first skip set will eliminate multiples of 2 as potential primes. """
        pp += 1
        """ Advance to the first potential prime, which is 3. """
        rss = [ss[0]]
        """ Initialize an array for the ranges of each skip set, setting the first member to be the range 
        of the first skip set, which is (ss[0]=2). Future skip sets will have ranges which can be 
        calculated, and are the sum of the members of the skip set. Another method of calculating the range 
        will also be shown below. """
        tp = [pp]
        """ Initialize an array for primes which are needed to verify potential primes against, setting the 
        first member as (pp=3), since we do not yet have a skip set that excludes multiples of 3. Also note 
        that 3 is a verified prime, without testing, since there are no primes less than the square root of 
        3. """
        i = 0
        """ Initialize a variable for keeping track of which skip set range is current. """
        rss.append(rss[i] * tp[0])
        """ Add a member to the array of skip set ranges, the value being the value of the previous skip 
        set range, (rss[0]=2), multiplied by the value of the largest prime which the new skip set will 
        exclude multiples of, (tp[0]=3), so 2*3=6. This value is needed to define when to begin 
        constructing the next skip set. """
        xp = []
        """ Initialize an array for extended primes which are larger than the square root of the user 
        defined limit (lim) and not needed to verify potential primes against, leaving it empty for now. 
        Again, the use of an extended primes array is technically unnecessary, but helps to clarify that we 
        have minimized the size of the test prime array. """
        pp += ss[0]
        """ Advance to the next potential prime, which is the previous potential prime, (pp=3), plus the 
        value of the next member of the skip set, which has only one member at this time and whose value is 
        (ss[0]=2), so 3+2=5. """
        npp = pp
        """ Initialize a variable for the next potential prime, setting its value as (pp=5). """
        tp.append(npp)
        """ Add a member to the array of test primes, the member being the most recently identified prime, 
        (npp=5). Note that 5 is a verified prime without testing, since there are no TEST primes less than 
        the square root of 5. """
        while npp < int(lim):
            """ Loop until the user defined upper limit is reached. """
            i += 1
            """ Increment the skip set range identifier. """
            while npp < rss[i] + 1:
                for n_n in ss:

                    npp = pp + n_n
                    """ Assign the next potential prime the value of the potential prime plus 
                     the value of the current member of the skip set. """
                    if npp > int(lim): break
                    """ If the next potential prime is greater than the user defined limit, 
                     then end the 'for n_n' loop. """
                    if npp <= rss[i] + 1: pp = npp
                    """ If the next potential prime is still within the range of the next skip 
                     set, then assign the potential prime variable the value of the next 
                    potential prime. Otherwise, the potential prime variable is not changed 
                     and the current value remains the starting point for constructing the next 
                     skip set. """
                    sqrtnpp = sqrt(npp)
                    """ Get the square root of the next potential prime, which will be the 
                    limit for the verification process. """
                    test = True
                    """ Set the verification flag to True. """
                    for q in tp:
                        if sqrtnpp < q:
                            break
                        elif npp % q == 0:
                            test = False
                            """ Then set the verification flag to False since the next 
                            potential prime is not a prime number. """
                            break
                            """ And end testing through the 'for q' loop. """
                        """ Otherwise, continue testing through the 'for q' loop. """
                    if test:
                        if npp <= sqrtlim:
                            tp.append(npp)
                        else:
                            xp.append(npp)
                            if len(xp) > 10000:
                                f.write('\n_n' + str(xp).strip('[').strip(']'))
                                xp = []

                        """ Otherwise, add it to the array of primes not needed to verify 
                         potential primes against. """
                    """ Then continue through the 'for n_n' loop. """
                if npp > int(lim): break
                """ If the next potential prime is greater than the user defined limit, then end 
                 the 'while npp<rss[i]+1' loop. """
                """ Otherwise, continue the 'while npp<rss[i]+1' loop. """
            if npp > int(lim): break
            """ If the next potential prime is greater than the user defined limit, then end the 'while 
             npp<int(lim)' loop. """
            """ At this point, the range of the next skip set has been reached, so we may begin
            constructing a new skip set which will exclude multiples of primes up through the value of 
            the first member of the test prime set, (tp[0]), from being selected as potential 
            primes. """
            lrpp = pp
            """ Initialize a variable for the last relevant potential prime and set its value to the 
             value of the potential prime. """
            nss = []
            """ Initialize an array for the next skip set, leaving it empty for now. """
            while pp < (rss[i] + 1) * 2 - 1:
                for n_n in ss:
                    npp = pp + n_n
                    """ Assign the next potential prime the value of the potential prime plus 
                     the value of the current member of the skip set. """
                    if npp > int(lim): break
                    """ If the next potential prime is greater than the user defined limit, 
                     then end the 'for n_n' loop. """
                    sqrtnpp = sqrt(npp)
                    """ Get the square root of the next potential prime, which will be the 
                    limit for the verification process. """
                    test = True
                    """ Set the verification flag to True. """
                    for q in tp:
                        if sqrtnpp < q:
                            break
                        elif npp % q == 0:
                            test = False
                            """ Then set the verification flag to False since the next 
                             potential prime is not a prime number. """
                            break
                            """ And end testing through the 'for q' loop. """
                        """ Otherwise, continue testing through the 'for q' loop. """
                    if test:
                        if npp <= sqrtlim:
                            tp.append(npp)
                        else:
                            xp.append(npp)
                            if len(xp) > 10000:
                                f.write('\n_n' + str(xp).strip('[').strip(']'))
                                xp = []

                        """ Otherwise, add it to the array of primes not needed to verify 
                         potential primes against. """
                    if npp % tp[0] != 0:
                        nss.append(npp - lrpp)
                        """ Add a member to the next skip set, the value of which is the 
                         difference between the last relevant potential prime and the next 
                         potential prime. """
                        lrpp = npp
                        """ Assign the variable for the last relevant potential prime the 
                         value of the next potential prime. """
                    pp = npp
                    """ Assign the variable for the potential prime the value of the next 
                     potential prime. """
                    """ Then continue through the 'for n_n' loop. """
                if npp > int(lim): break
                """ If the next potential prime is greater than the user defined limit, then end 
                 the 'while npp<(rss[i]+1)*2-1' loop. """
                """ Otherwise, continue the 'while npp<(rss[i]+1)*2-1' loop. """
            if npp > int(lim): break
            """ If the next potential prime is greater than the user defined limit, then end the 'while 
             npp<int(lim)' loop. """
            ss = nss
            """ Assign the skip set array the value of the new skip set array. """
            ep.append(tp[0])
            """ Add a new member to the excluded primes array, since the newly constructed skip set 
             will exclude all multiples of primes through the first member of the test prime array. """
            del tp[0]
            """ Delete the first member from the test prime array since future potential primes will 
             not have to be tested against this prime. """
            rss.append(rss[i] * tp[0])
            """ Add a member to the skip set range array with the value of the range of the next skip 
             set. """
            npp = lrpp
            """ Assign the next potential prime the value of the last relevant potential prime. """
            """ Then continue through the 'while npp<int(lim)' loop. """
        """ At this point the user defined upper limit has been reached and the generator has completed 
        finding all of the prime numbers up to the user defined limit. """
        ep.reverse()
        """ Flip the array of excluded primes. """
        [tp.insert(0, a) for a in ep]
        """ Add each member of the flipped array into the beginning of the test primes array. """
        tp.reverse()
        """ Flip the array of test primes. """
        xp = []
        [xp.insert(0, a) for a in tp]
        f.write('\n_n\n_n' + str(xp).strip('[').strip(']'))
        """ Add each member of the flipped array into the beginning of the extended primes array. """
        return xp
    """ Send the completed array of all primes up to the user defined limit back to the function call. """


def primes3(limit):
    """
    Generate a list containing all primes below limit.
    """
    t = ((limit + 1) / 2)
    sieve = [True] * t
    sieve[0] = False
    for p in range(3, int(limit ** 0.5) + 1, 2):  # Handle odd numbers only
        if sieve[p // 2]:
            m = (limit // p - p) // 2 + 1
            sieve[p * p // 2::p] = [False] * m
    return [2] + [2 * p + 1 for p, val in enumerate(sieve) if val]


'''
def P10(n_n):
    #sum of primes up to n_n
    r = int(n_n**0.5)
    assert r*r <= n_n and (r+1)**2 > n_n
    V = [n_n//i for i in range(1,r+1)]
    V += list(range(V[-1]-1,0,-1))
    S = {i:i*(i+1)//2-1 for i in V}
    for p in range(2,r+1):
        if S[p] > S[p-1]:  # p is prime
            sp = S[p-1]  # sum of primes smaller than p
            p2 = p*p
            for v in V:
                if v < p2: break
                S[v] -= p*(S[v//p] - sp)
    return S[n_n]
'''


def primesfrom2to(n_n):
    import numpy
    """ Input n_n>=6, Returns a array of primes, 2 <= p < n_n """
    sieve = numpy.ones(n_n / 3 + (n_n % 6 == 2), dtype=numpy.bool)
    for i in xrange(1, int(n_n ** 0.5) / 3 + 1):
        if sieve[i]:
            k = 3 * i + 1 | 1
            sieve[k * k / 3::2 * k] = False
            sieve[k * (k - 2 * (i & 1) + 4) / 3::2 * k] = False
    return numpy.r_[2, 3, ((3 * numpy.nonzero(sieve)[0][1:] + 1) | 1)]


def atkins13(limit=1000000):
    """use sieve of atkins to find primes <= limit."""
    primes = [0] * limit

    # n_n = 3x^2 + y^2 section
    xx3 = 3
    for dxx in xrange(0, 12 * int(sqrt((limit - 1) / 3)), 24):
        xx3 += dxx
        y_limit = int(12 * sqrt(limit - xx3) - 36)
        n_n = xx3 + 16
        for dn in xrange(-12, y_limit + 1, 72):
            n_n += dn
            primes[n_n] = not primes[n_n]

        n_n = xx3 + 4
        for dn in xrange(12, y_limit + 1, 72):
            n_n += dn
            primes[n_n] = not primes[n_n]

    # n_n = 4x^2 + y^2 section
    xx4 = 0
    for dxx4 in xrange(4, 8 * int(sqrt((limit - 1) / 4)) + 4, 8):
        xx4 += dxx4
        n_n = xx4 + 1

        if xx4 % 3:
            for dn in xrange(0, 4 * int(sqrt(limit - xx4)) - 3, 8):
                n_n += dn
                primes[n_n] = not primes[n_n]

        else:
            y_limit = 12 * int(sqrt(limit - xx4)) - 36

            n_n = xx4 + 25
            for dn in xrange(-24, y_limit + 1, 72):
                n_n += dn
                primes[n_n] = not primes[n_n]

            n_n = xx4 + 1
            for dn in xrange(24, y_limit + 1, 72):
                n_n += dn
                primes[n_n] = not primes[n_n]

    # n_n = 3x^2 - y^2 section
    xx = 1
    for x in xrange(3, int(sqrt(limit / 2)) + 1, 2):
        xx += 4 * x - 4
        n_n = 3 * xx

        if n_n > limit:
            min_y = ((int(sqrt(n_n - limit)) >> 2) << 2)
            yy = min_y * min_y
            n_n -= yy
            s = 4 * min_y + 4

        else:
            s = 4

        for dn in xrange(s, 4 * x, 8):
            n_n -= dn
            if n_n <= limit and n_n % 12 == 11:
                primes[n_n] = not primes[n_n]

    xx = 0
    for x in xrange(2, int(sqrt(limit / 2)) + 1, 2):
        xx += 4 * x - 4
        n_n = 3 * xx

        if n_n > limit:
            min_y = ((int(sqrt(n_n - limit)) >> 2) << 2) - 1
            yy = min_y * min_y
            n_n -= yy
            s = 4 * min_y + 4

        else:
            n_n -= 1
            s = 0

        for dn in xrange(s, 4 * x, 8):
            n_n -= dn
            if n_n <= limit and n_n % 12 == 11:
                primes[n_n] = not primes[n_n]

    # eliminate squares        
    for n_n in xrange(5, int(sqrt(limit)) + 1, 2):
        if primes[n_n]:
            for k in range(n_n * n_n, limit, n_n * n_n):
                primes[k] = False

    return [2, 3] + filter(primes.__getitem__, xrange(5, limit, 2))
