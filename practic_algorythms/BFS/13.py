"""
практика по алгоритму поиска в ширину, день 12
"""


def BFS(graph, start_dot):
    visited = []
    queue = [start_dot]

    while queue:
        this = queue.pop(0)
        if this not in visited:
            visited.append(this)

            neighbors = graph[this]
            for neighbour in neighbors:
                queue.append(neighbour)

    return visited