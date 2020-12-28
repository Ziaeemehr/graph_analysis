import numpy as np 
import igraph 
import networkx as nx

G = nx.gnp_random_graph(100, 0.04, directed=True)
adj = nx.to_numpy_array(G, dtype=int)

# adj = np.loadtxt("adj.txt", dtype=int)
conn_indices = np.where(adj)
weights = adj[conn_indices]
edges = list(zip(*conn_indices))
G = igraph.Graph(edges=edges, directed=True)
# print(G.summary())
print(G.is_connected())

print(G.clusters())