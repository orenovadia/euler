import eulertools

s_dig_pandigital = eulertools.c_sum_of_digits(123456789)
mulz = []
for i in range(1,100):
    mulz.append(
        sum(range(1,i))
    )
print mulz
