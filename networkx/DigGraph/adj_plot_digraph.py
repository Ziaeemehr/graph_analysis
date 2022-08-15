import networkx as nx 
import pylab as plt
import numpy as np 

G = nx.DiGraph()
G.add_edge(0, 1)
G.add_edge(1, 2)

print(G.edges())
adj = nx.to_numpy_array(G, dtype=int)
print(adj)

plt.imshow(adj, origin='lower')
plt.xticks([0,1,2])
plt.yticks([0,1,2])
plt.ylabel("FROM")
plt.xlabel("TO")
plt.show()
# outward edges on rows
# [(0, 1), (1, 2)]
# [[0 1 0]
#  [0 0 1]
#  [0 0 0]]
