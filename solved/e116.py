def cached(f):
    cache = {}

    def decorator(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]

    return decorator


@cached
def n_sequences(score, possible_scores):
    if score == 0:
        return 1
    if score < 0:
        return 0
    return sum(n_sequences(score - play, possible_scores) for play in possible_scores)


# question 116:
N = 50
# Must subtract 1 on account of just '1' tiles
print n_sequences(N, (4, 1,)) + n_sequences(N, (3, 1)) + n_sequences(N, (2, 1)) - 3

# question 117:
N = 50
print n_sequences(N, (4, 3, 2, 1,))
