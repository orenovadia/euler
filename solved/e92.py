from eulertools import square_sum_of_digits

'''
performance:
well, with the square sum of digits function written in c:
real	0m17.096s
user	0m16.499s
sys	0m0.537s

and for this function written in python:
def square_sum_of_digits(x):
    return sum([int(i) ** 2 for i in str(x)])

{1: 1418853, 89: 8581146}

real	1m47.491s
user	1m46.454s
sys	0m0.764s
'''


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
