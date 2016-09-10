from itertools import chain, combinations, count

from euler.solved.eulertools import primes

p = primes(1000)
prime_set  =set(p)
more_primes = set(primes(1000000))

def quick_is_prime(n):
    global prime_set
    if n in prime_set:
        return True
    if n in more_primes:
        return True
    return False

def check_couple(a,b):
    for i in count(0):
        q = i**2 + a*i + b
        if not quick_is_prime(q):
            break
    return i


def main():
    max_produced = 0
    all_ps = list(chain(p, [-i for i in p]))
    combs = combinations(all_ps, 2)
    for a,b in combs:
        produced = max(check_couple(a,b), check_couple(b,a))
        if produced>max_produced:
            print produced,a,b,a*b
            max_produced=produced


if __name__ == '__main__':
    main()