import eulertools

N = 5000
p_list = range(1,100)


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
    return s

def main(N):
    a = e77_iterate(100,99)
    print
    print
    print a


if __name__ == '__main__':
    main(N)
