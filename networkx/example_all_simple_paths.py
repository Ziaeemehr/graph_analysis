import numpy as np
import pylab as plt
# https://testfixsphinx.readthedocs.io/en/latest/_modules/networkx/algorithms/simple_paths.html
import networkx as nx

G = nx.complete_graph(4)
# for path in nx.all_simple_paths(G, source=0, target=3):
#     print(path)

G = nx.gnp_random_graph(5, 0.8, directed=True, seed=2)
for path in nx.all_simple_paths(G, source=0, target=3):
    print(path)

pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True)
plt.show()