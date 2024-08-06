"""
Реализация графа
"""

import networkx as nx

G = nx.Graph()

G.add_node("Mike")  # Добавлем вершину
G.add_nodes_from(["Amine", "Wassim", "Nick"])  # Добавляем группу вершин
G.add_edge("Mike", "Amine")  # Добавляем ребро между существующими вершинами

print(list(G.nodes))
print(list(G.edges))