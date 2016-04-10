import eulertools

N = 1000000
pp = eulertools.primes2(N)


def generate_permutations(p):
    n_digits = len(str(p))
    l = set([p])

    for i in xrange(n_digits - 1):
        lsd = p % 10
        p = p / 10 + lsd * 10 ** (n_digits-1)
        l.add(p)
    return l

s=0
while pp:
    p = pp[0]
    okay  = True
    permutations  = generate_permutations(p)
    n_perm = len(permutations)
    for permutation in permutations:
        if permutation in pp:
            pp.remove(permutation)
        else:
            okay = False
            break
    if okay:
        print p,
        s += n_perm
    else:
        try: pp.remove(p)
        except:pass
print
print s