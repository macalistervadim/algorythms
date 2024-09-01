"""
Практика по алгоритму сортировки в глубину, день 8
"""

from typing import Mapping


def DFS(
    graph: Mapping[str, set[str]],
    startDot: str,
    visited: set[str] | None = None,
) -> set[str]:
    if not visited:
        visited = set()

    visited.add(startDot)

    for i in graph[startDot] - visited:
        DFS(graph, i, visited)

    return visited
