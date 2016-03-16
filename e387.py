import gmpy2

N = 10 ** 14
is_prime = gmpy2.is_prime


def is_harshad_number(n):
    sum_of_digits = sum([int(i) for i in str(n)])
    return n % sum_of_digits == 0


def is_strong_harshad_number(n):
    if n < 10:
        return False
    sum_of_digits = sum([int(i) for i in str(n)])
    return (n % sum_of_digits == 0) and is_prime(n / sum_of_digits)


def recurr(start_from, N=N):
    if start_from > N:
        return 0
    sum = 0
    if is_prime(start_from):
        if is_strong_harshad_number(start_from / 10):
            sum += start_from
            #print start_from
    if not is_harshad_number(start_from):
        return sum
    for i in range(10):
        sum += recurr(start_from * 10 + i, N)
    return sum


def main(N):
    sum = 0
    for i in range(1, 10):
        sum += recurr(i)
    print '-' * 30
    print sum,'N=',N


if __name__ == '__main__':
    main(N)
