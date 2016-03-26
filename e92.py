from eulertools import square_sum_of_digits


# def square_sum_of_digits(x):
#     return sum([int(i) ** 2 for i in str(x)])


def is_89_or_1(n):
    global d, sols
    if n in d:
        return d[n]
    ret = is_89_or_1(
        square_sum_of_digits(n)
    )
    d[n] = ret  # cache the answer for this number
    sols[ret] += 1  # increase count for 1 or 89
    return ret


d = {}
d[1] = 1
d[89] = 89

sols = {}
sols[1] = 1
sols[89] = 1

N = 10 ** 7
for i in xrange(1, N):
    is_89_or_1(i)

print sols
