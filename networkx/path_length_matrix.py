'''
Networkx: Get the distance between nodes and make a distance matrix
'''

import numpy as np
import networkx as nx
from sys import exit


def shortest_path_length_matrix_u(G):
    """
    return distance between nodes in a 2d numpy array
    in an undirected and unweighted graph
    """
    N = G.number_of_nodes()
    distance_mat = np.zeros((N, N), dtype=int)

    L = list(nx.shortest_path_length(G, weight=None))
    for i in range(N):
        for j, value in L[i][1].items():
            distance_mat[i][j] = value

    return distance_mat


G = nx.path_graph(5)
D = shortest_path_length_matrix_u(G)
print(D)
