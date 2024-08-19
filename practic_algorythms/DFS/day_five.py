"""
Практика по алгоритму сортировки в глубину, день 5
"""

from typing import Mapping


graph = {
    "Amin": {"Wasim", "Nick", "Mike"},
    "Wasim": {"Imran", "Amin"},
    "Imran": {"Wasim", "Faras"},
    "Faras": {"Imran"},
    "Mike": {"Amin"},
    "Nick": {"Amin"},
}


def BFS(
    graph: Mapping[str, set[str]],
    startDot: str,
    visited: set[str] | None = None,
) -> set[str]:
    if not visited:
        visited = set()

    visited.add(startDot)

    for i in graph[startDot] - visited:
        BFS(graph, i, visited)

    return visited
