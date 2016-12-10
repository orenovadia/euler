import networkx as nx


def load_matrix():
    filename = 'p107_network_example.txt'
    filename = 'p107_network.txt'
    with open(filename) as f:
        return map(lambda row: [int(x.strip()) for x in row.strip().replace('-', '0').split(',')], f.readlines())


def load_graph():
    g = nx.Graph()
    matrix = load_matrix()
    for i, row in enumerate(matrix):
        for j, weight in enumerate(row):
            if weight:
                g.add_edge(i, j, weight=weight)
    return g


def omega(g):
    return sum(data['weight'] for _, _, data in g.edges_iter(data=True))


def main():
    g = load_graph()
    initial_weight = omega(g)
    print 'initial weight', initial_weight
    N = len(g.node)
    print 'Nodes: ', N

    optimal = nx.Graph()
    node = next(g.nodes_iter())
    optimal.add_node(node)

    while len(optimal.node) < N:
        edges = sorted(g.edges_iter(nbunch=optimal.node, data=True), key=lambda d: d[2]['weight'])
        min_edge = next(e for e in edges if e[1] not in optimal.node)
        optimal.add_node(min_edge[1])
        optimal.add_edge(*min_edge)

    optimal_weight = omega(optimal)
    print 'optimal weight:', optimal_weight
    print 'reduced weight:', initial_weight - optimal_weight


if __name__ == '__main__':
    main()
