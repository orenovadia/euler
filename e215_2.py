from typing import Tuple, Set, List

BRICK_SIZES = (2, 3)


def main(h=10, w=32):
    possible_layers = list(gen_layers(w))
    crack_locations = list(map(cracks_of, possible_layers))
    layer_adjacency = build_adjacency(crack_locations)
    print(calc_ways(layer_adjacency, h))


def gen_layers(total_width):
    """
    dfs over different sequences of bricks.
    """
    stack = [(0, ())]  # stack of (width, (tuple of brick sizes))

    while stack:
        width, bricks = stack.pop()
        if width == total_width:
            yield bricks
            continue
        if width > total_width:
            continue
        for next_ in BRICK_SIZES:
            stack.append((width + next_, bricks + (next_,)))


def cracks_of(layer):
    # type: (Tuple[int,...]) -> Set[int]
    """
    Location of all the cracks of a layer besides the start and end.
    """

    def gen():
        # cumulative sum besides last element
        s = 0
        for i in layer[:-1]:
            s += i
            yield s

    return set(gen())


def build_adjacency(cracks):
    # type: (List[Set[int]]) -> List[List[int]]
    """
    For given cracks, build a graph signifying which layers can be placed adjacent to one another.
    This is done by looking at the intersection of all pairs of layers.
    """
    return [
        [other_idx for other_idx in range(len(cracks))
         if len(this & cracks[other_idx]) == 0]
        for this in cracks
    ]


def calc_ways(adjacency, h):
    """
    We use DP to calculate all possible walls.
    We build the wall from bottom to top where (Li is one type of brick layer):
    f(height, Li) = sum of f(height - 1, Lj)
                    for all Lj that can be placed under Li

    At the end we sum all f(h, Li) for all i
    """
    # current_floor[i] is number of ways to build a wall of current height
    # with layer `i` at the top, we start with the first floor (one way to build it).
    current_floor = [1 for _ in adjacency]

    for _ in range(1, h):
        next_floor = [
            sum(current_floor[other] for other in adjacency[i])
            for i in range(len(adjacency))
        ]
        current_floor = next_floor

    return sum(current_floor)


if __name__ == '__main__':
    main()
