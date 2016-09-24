import itertools


def get_all_combinations_for_k_tuple(k, current_l=0, curr_list=None):
    if current_l == k:
        # if sum(curr_list) == reduce(int.__mul__, curr_list, 1):
        yield tuple(curr_list)
        raise StopIteration()
    for j in range(1, 10):
        curr_list[current_l] = j
        # if sum(curr_list) < reduce(int.__mul__, curr_list, 1):
        #     raise StopIteration()
        for y in get_all_combinations_for_k_tuple(k, current_l=current_l + 1, curr_list=curr_list):
            yield y


def minimize_for_k(k):
    min_tup = None
    for k_tuple in get_all_combinations_for_k_tuple(k, curr_list=[1] * k):
        if sum(k_tuple) < reduce(int.__mul__, k_tuple, 1):
            break
        if sum(k_tuple) == reduce(int.__mul__, k_tuple, 1):
            if sum(min_tup)
            return k_tuple
    # return min(k_tuple, key=sum)


for k in range(2, 20):
    combo = minimize_for_k(k)
    print k, sum(combo), combo
