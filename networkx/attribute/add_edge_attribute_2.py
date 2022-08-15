import networkx as nx
import numpy as np


G = nx.DiGraph()

G.add_edge(0, 1, delay=1)
G.add_edge(1, 2, delay=2)

G[0][1]['weight'] = 0.5

print(G.edges(data=True))