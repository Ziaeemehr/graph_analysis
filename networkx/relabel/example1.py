import networkx as nx
from pprint import pprint


G = nx.gnp_random_graph(n=10, p=0.3, seed=1)

# pprint(nx.to_numpy_array(G, dtype=int))

print("(label, degree)")
print(nx.degree(G))

# reverse=True for decending order
sorted_degrees = sorted(G.degree, key=lambda x: x[1], reverse=False)
print("sorted nodes based on their degrees:")
print(sorted_degrees)

new_labels = [x[0] for x in sorted_degrees]
print("new labels")
print(new_labels)
# new_labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g','h', 'i', 'j']

mapping = dict(zip(G, new_labels))
print("mapping")
print(mapping)

H = nx.relabel_nodes(G, mapping, copy=True)


# reverse=True for decending order
# sorted_degrees = sorted(H.degree, key=lambda x: x[1], reverse=False)
# print("sorted nodes based on their degrees:")
# print(sorted_degrees)

# print("="*70)
# print("G: ", nx.degree(G))
# print("H: ", nx.degree(H))

# sorted_ = sorted(H.degree, key=lambda x: x[1], reverse=False)
# print("sorted nodes")
# print(sorted_)

# sorted_ = sorted(H.degree, key=lambda x: x[0], reverse=False)
# print("sorted nodes")
# print(sorted_)