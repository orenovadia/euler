from itertools import permutations

l = range(1, 10)[::-1]
perms = permutations(l)
sum_9 = sum(range(1, 10))
set_1_9 = set(range(1, 10))


def is_pandigital(x):
    digs = map(int, str(x))
    if sum(digs) != sum_9:
        return False
    return set(digs) == set_1_9


def can_become_pandigital(x):
    if x > 987654321:
        return False
    digit_set = set(map(int, str(x)))
    l = sorted(digit_set)
    max_x = sum(d * 10 ** i for i, d in enumerate(l))
    return x <= max_x
max_nip = 123456789
for candidate in range(1, int(10 ** 4.6)):
    n=1
    number = candidate
    while can_become_pandigital(number):
        if is_pandigital(number):
            if number>max_nip:
                max_nip = number
            break
        n+=1
        number = number * 10 **len(str(candidate*n))
        number += candidate*n
print max_nip