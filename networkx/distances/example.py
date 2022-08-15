import numpy as np 
from time import time
import networkx as nx 

N = 10
p = 0.6
# seed = 2
g1 = nx.gnp_random_graph(N, p)
g2 = nx.gnp_random_graph(N, p)


start = time()
# print(nx.graph_edit_distance(g1, g2))
# print(nx.optimize_graph_edit_distance(g1, g2))
for v in nx.optimize_graph_edit_distance(g1, g2):
    minv = v
print(minv)
print("Done in {:g}".format(time()-start))


