"""
Практика по алгоритму поиска в ширину, день 8
"""

from typing import Mapping


def BFS(graph: Mapping[str, set[str]], startDot: str) -> list[str]:
    visited = []
    queue = [startDot]

    while queue:
        this = queue.pop(0)
        if this not in visited:
            visited.append(this)

            neighbours = graph[this]
            for neighbour in neighbours:
                queue.append(neighbour)

    return visited
