import sys

import networkx as nx
from itertools import permutations


def cycle_length(g, cycle):
    assert len(cycle) == g.number_of_nodes()
    weight = g.edges[cycle[0], cycle[-1]]['weight']
    for i in range(0, len(cycle) - 1):
        weight += g.edges[cycle[i], cycle[i + 1]]['weight']

    return weight


# Here is a test case:
# Create an empty graph.
G = nx.Graph()
# Now we will add 6 edges between 4 vertices
G.add_edge(0, 1, weight=2)
G.add_edge(1, 2, weight=2)
G.add_edge(2, 3, weight=2)
G.add_edge(3, 0, weight=2)
G.add_edge(0, 2, weight=1)
G.add_edge(1, 3, weight=1)

# Now we want to compute the lengths of two cycles:
cycle1 = [0, 1, 2, 3]
cycle2 = [0, 2, 1, 3]

assert (cycle_length(G, cycle1) == 8)
assert (cycle_length(G, cycle2) == 6)


def all_permutations(g):
    n = g.number_of_nodes()
    shortest_weight = sys.maxsize
    for cycle in permutations(range(n)):
        weight = cycle_length(g, cycle)
        if weight < shortest_weight:
            shortest_weight = weight

    return shortest_weight


print(all_permutations(G))


def average(g):
    # n is the number of vertices.
    n = g.number_of_nodes()

    # Sum of weights of all n*(n-1)/2 edges.
    sum_of_weights = sum(g[i][j]['weight'] for i in range(n) for j in range(i))

    avg_wt = 2 * sum_of_weights / (n - 1)
    return avg_wt


def nearest_neighbors(g):
    current_node = 0
    path = [current_node]
    n = g.number_of_nodes()

    # We'll repeat the same routine (n-1) times
    unvisited_nodes = list(g.nodes)
    for _ in range(n - 1):
        unvisited_nodes.remove(current_node)
        next_node = None
        # The distance to the closest vertex. Initialized with infinity.
        min_edge = float("inf")
        for v in unvisited_nodes:
            weight = g.edges[current_node, v]['weight']
            if weight < min_edge:
                min_edge = weight
                next_node = v
            # Write your code here: decide if v is a better candidate than next_node.
            # If it is, then update the values of next_node and min_edge
        assert next_node is not None
        path.append(next_node)
        current_node = next_node

    weight = sum(g[path[i]][path[i + 1]]['weight'] for i in range(g.number_of_nodes() - 1))
    weight += g[path[-1]][path[0]]['weight']
    return weight

print(nearest_neighbors(G))
