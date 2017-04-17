from itertools import product


def is_triangle(number):
    m = (number * 2) ** 0.5
    m_n = int(m) * (int(m) + 1) / 2 == number
    return m_n or int(m) * (int(m) - 1) / 2 == number


guess = 2 * 3 * 5 * 7 * 11 * 13 * 17
for e2, e3, e5, e7, e19, e23 in product(range(7), range(7), range(7), range(7), range(2), range(2)):
    n = guess * 2 ** e2 * 3 ** e3 * 5 ** e5 * 7 ** e7 * 19 ** e19 * 23 ** e23
    if is_triangle(n):
        print(n, (e2, e3, e5, e7, e19, e23))

