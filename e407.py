def a_sqr_mod_n(a, n):
    return (a ** 2) % n


def brute_m_of_n(n):
    return max(xrange(n), key=lambda a: a if a == a_sqr_mod_n(a, n) else 0)


def brute_sigma_m_of_n(N):
    return sum(brute_m_of_n(n) for n in range(1, N + 1))


def less_brute_m_of_n(N):
    squares = [i ** 2 for i in xrange(N + 1)]
    s = 0
    for n in xrange(1, N + 1):
        for a in xrange(n - 1, 0, -1):
            if a == squares[a] % n:
                s += a
                break
    return s


# 4**2 - 4 = 12 , 6 is the highest divisor of 12 that is larger than 4
def smallest_divisors_higher_then_a(a):
    a_square_minus_a = a ** 2 - a
    for candidate in xrange(a + 1, a_square_minus_a):
        if a_square_minus_a % candidate == 0:
            return candidate
    return 0


def check_idempotents_for_higher_n_method(N):
    candidate_cache = [1 for _ in xrange(N + 1)]
    candidate_cache[0] = 0
    candidate_cache[1] = 0
    for a in xrange(1, N + 1):
        fac = smallest_divisors_higher_then_a(a)
        if not fac or fac > N:
            continue
        for n_to_set in xrange(fac, N + 1, fac):
            candidate_cache[n_to_set] = a
    return sum(candidate_cache)

if __name__ == '__main__':
    m = 20
    print 'N =', m
    print range(1,m+1)
    print map(brute_m_of_n,range(1,m+1))
    # print less_brute_m_of_n(m)
    print check_idempotents_for_higher_n_method(m)
