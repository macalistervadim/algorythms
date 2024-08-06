"""
Алгоритм PageRank

Задача данного алгоритма - поиск наилучшего способа измерения релевантности веб-страниц,
возвращаемых в результат запроса
"""


import numpy as np
import networkx as nx
import matplotlib.pyplot as plt


myWeb = nx.DiGraph()
myPages = range(1, 6)

connections = [
    (1, 3), (2, 1), (2, 3), (3, 1), (3, 2), (3, 4), (4, 5), (5, 1), (5, 4),
]
myWeb.add_nodes_from(myPages)
myWeb.add_edges_from(connections)


pos = nx.shell_layout(myWeb)
nx.draw(myWeb, pos, arrows=True, with_labels=True)
plt.show()


def createPageRank(aGraph):
    nodesSet = len(aGraph)
    M = nx.to_numpy_array(aGraph)
    outwards = np.squeeze(np.asarray(np.sum(M, axis=1)))
    probOutwards = np.array(
        [1.0/count if count > 0 else 0.0 for count in outwards]
    )
    G = np.asarray(np.multiply(M.T, probOutwards))
    p = np.ones(nodesSet) / float(nodesSet)
    if np.min(np.sum(G, axis=0)) < 1.0:
        print("WARN: G is substochastic")
    return G, p


G, p = createPageRank(myWeb)
print(G)
