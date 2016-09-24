def inverse(n):
    return int(str(n)[::-1])


def is_palindrom(n):
    return n == inverse(n)


def is_lychrel(n, depth=0):
    if depth >= 50:
        return False
    new_n = inverse(n) + n
    print new_n
    return is_palindrom(new_n) or is_lychrel(new_n, depth=depth + 1)


if __name__ == '__main__':
    s = 0
    # print is_lychrel(196)
    for i in xrange(1, 10000):
        if not is_lychrel(i):
            s += 1
    print  s
