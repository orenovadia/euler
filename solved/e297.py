from itertools import takewhile
from linecache import cache

from cachetools import cached


def fib():
    a = 1
    b = 2
    yield a
    while True:
        a, b = b, a + b
        yield a


def e267(n):
    fibs = tuple(takewhile(lambda f: f <= n, fib()))  # all fib numbers under n
    print('collected {} fib numbers smaller than {}'.format(len(fibs), n))

    n_f_to_triangle_sum = {}

    @cache(n_f_to_triangle_sum)
    def sigma_z_up_to(n_f):
        if n_f == 0:
            return 1
        if n_f == 1:
            return 2
        return fibs[n_f - 1] + sigma_z_up_to(n_f - 1) + sigma_z_up_to(n_f - 2)

    sigma_z_up_to(len(fibs) - 1)
    width_to_triangle_sum = {sum(fibs[:k[0]]) + 1: v for k, v in n_f_to_triangle_sum.items()}

    space_left = n - 1
    result = 0

    while space_left > 0:
        if space_left in width_to_triangle_sum:
            print('found triangle of width', space_left)
            result += width_to_triangle_sum[space_left]
            break
        max_width_to_take = max(filter(lambda item: item < space_left, width_to_triangle_sum.keys()))
        space_left = space_left - max_width_to_take
        result += width_to_triangle_sum[max_width_to_take] + space_left
        space_left -= 1
        print('space_left', space_left, 'result', result)

    print(result)


if __name__ == '__main__':
    e267(10 ** 17)
