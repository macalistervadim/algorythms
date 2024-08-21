"""
Практика по алгоритму поиска в глубину, день 6
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


def DFS(
    graph: Mapping[str, set[str]],
    startDot: str,
    visited: set[str] | None = None
) -> set[str]:
    if not visited:
        visited = set()

    visited.add(startDot)

    for i in graph[startDot] - visited:
        DFS(graph, i, visited)

    return visited


print(DFS(graph, "Amin"))
