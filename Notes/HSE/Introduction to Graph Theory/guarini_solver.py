import networkx as nx
import itertools as it

G = nx.Graph()

for wb_indices in it.permutations(range(8), 4):
    configuration = ['*'] * 8
    configuration[wb_indices[0]] = 'W'
    configuration[wb_indices[1]] = 'W'
    configuration[wb_indices[2]] = 'B'
    configuration[wb_indices[3]] = 'B'

    G.add_node("".join(configuration))

moves = [[] for _ in range(8)]
moves[0] = [4, 6]
moves[1] = [5, 7]
moves[2] = [3, 6]
moves[3] = [2, 7]
moves[4] = [0, 5]
moves[5] = [1, 4]
moves[6] = [0, 2]
moves[7] = [1, 3]

for node in G.nodes():
    configuration = [c for c in node]

    for i in range(8):
        if configuration[i] != "*":
            for new_pos in moves[i]:
                if configuration[new_pos] != "*":
                    continue
                new_configuration = list(configuration)

                new_configuration[i] = "*"
                new_configuration[new_pos] = configuration[i]

                if not G.has_edge("".join(configuration), "".join(new_configuration)):
                    G.add_edge("".join(configuration), "".join(new_configuration))

print(nx.number_of_nodes(G))
print(nx.number_of_edges(G))
print(nx.number_connected_components(G))

assert "W*B**W*B" in nx.node_connected_component(G, "W*W**B*B")
assert "B*B**W*W" in nx.node_connected_component(G, "W*W**B*B")
assert "W*B**B*W" not in nx.node_connected_component(G, "W*W**B*B")

print(" -> ".join(nx.shortest_path(G, "W*W**B*B", "B*B**W*W")))
