import networkx as nx
import numpy as np


G = nx.erdos_renyi_graph(5, 0.3, seed=125)
edges = G.edges()
attrs = {}
for e in G.edges():
    attrs[e] = {'delay': 10, 'weight': 0.5}

# print(attrs)
nx.set_edge_attributes(G, attrs)
print(nx.to_numpy_array(G, weight=None, dtype=int))
print(nx.to_numpy_array(G, weight='weight'))
print(nx.to_numpy_array(G, weight='delay', dtype=int))

# n = nx.number_of_nodes(G)
# print(G[0][2]['delay'])

# A = np.zeros((n, n))
# D = np.zeros((n, n))
# for e in edges:
#     A[e[0], e[1]] = A[e[1], e[0]] = G[e[0]][e[1]]['delay']
#     D[e[0], e[1]] = D[e[1], e[0]] = G[e[0]][e[1]]['weight']