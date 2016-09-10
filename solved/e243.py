from fractions import Fraction

from euler.eulertools import primes
# hcn list from here: https://web.archive.org/web/19980707182518/http://www.math.princeton.edu/~kkedlaya/math/
p = primes(10000)
lim = Fraction(15499, 94744)

print lim


def calc_n(pows):
    n = 1
    for q, pow in zip(p, pows):
        n *= q ** pow
    return n


def totient(n, pows):
    distinct_primes = p[:len(pows)]
    n = n
    for q in distinct_primes:
        n *= 1 - Fraction(1, q)
    return n


def totient_n_div_n(pows):
    distinct_primes = p[:len(pows)]
    n = 1
    for q in distinct_primes:
        n *= 1 - Fraction(1, q)
    return n


def main_iter_hcns():
    for i, row in enumerate(open('hcns')):
        tokens = row.split()
        if '+' in tokens[-1]:
            n_lasts = tokens.pop(-1)
            tokens.extend([1, ] * int(n_lasts[1:]))
        pows = map(int, tokens)
        n = calc_n(pows)
        t = totient_n_div_n(pows) * n
        ans = t / (n - 1)
        print lim, n, ans, ans - lim
        if i > 120:
            break


def main():
    n = 1
    tots = 1
    for i, q in enumerate(p[:200]):
        n *= q
        tots *= 1 - Fraction(1, q)
        totient_ = n * tots

        r_of_d = Fraction(tots * n, (n - 1))
        # print r_of_d < lim, i, n, r_of_d, float(r_of_d - lim)
        if r_of_d>lim:
            for new_p in range(2,20):
                new_n = n*new_p
                new_r_of_d = Fraction(tots * new_n, (new_n - 1))
                if new_r_of_d<lim:
                    print i, new_p, new_n
        # if tots < lim: #223092870
        # if r_of_d < lim: #223092870
        if i > 14:
            break


main()
