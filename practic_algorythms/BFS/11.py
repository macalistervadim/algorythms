"""
Практика по алгоритму поиску в ширину, день 11
"""


def BFS(graph, start_dot):
    visited = []
    queue = [start_dot]

    while queue:
        this = queue.pop(0)
        if this not in visited:
            visited.append(this)

            neighbours = graph[this]
            for neighbour in neighbours:
               queue.append(neighbour)

    return visited