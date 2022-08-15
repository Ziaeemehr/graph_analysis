import networkx as nx


G = nx.path_graph(3)  # nodes 0-1-2
print(G.nodes())
mapping = {0: "a", 1: "b"}  # 0->'a' and 1->'b'
G = nx.relabel_nodes(G, mapping, copy=True)
print(G.nodes())
