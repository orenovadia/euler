import itertools

li = 9


def list_of_digits_to_int(l):
    return int(''.join(l))


def slice(permut):
    global li
    s = 0
    for i in xrange(1, 6):
        for j in xrange(i+1, li):
            left = list_of_digits_to_int(permut[:i])
            right = list_of_digits_to_int(permut[i:j])
            n = list_of_digits_to_int(permut[j:])
            if left * right > n:
                continue
            elif left * right == n:
                s += n
    return s

if __name__ == '__main__':
    digs = list('123456789')
    s = 0
    sols = set()
    for i in itertools.permutations(digs):
        sols.add(slice(i))
        s += 1
    print s, 'permmutations'
    print sols, 'solutions'
    print sum(sols),len(sols)-1
