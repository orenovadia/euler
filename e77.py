import eulertools

N = 5000
p_list = eulertools.primes2(N)


def e77_iterate(destination, max_prime_used):
    s = 0
    if destination == 0:
        return 1
    if destination < 0:
        return 0
    else:
        for p in p_list:
            if destination - p < 0 or p > max_prime_used:
                return s
            s += e77_iterate(destination - p, p)


def main(N):
    for i in xrange(10, N):
        m = e77_iterate(i, i)
        if m > 5000:
            print i, m
            break


if __name__ == '__main__':
    main(N)
