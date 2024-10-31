"""
Практика по алгоритму поиска в глубину, день 9
"""

from typing import Mapping


def DFS(
    graph: Mapping[str, set[str]],
    start_dot: str,
    visited: set[str] | None = None,
) -> set[str]:
    if not visited:
        visited = set()

    visited.add(start_dot)

    for i in graph[start_dot] - visited:
        DFS(graph, i, visited)

    return visited


graph = {
    "Amin": {"Wasim", "Nick", "Mike"},
    "Wasim": {"Imran", "Amin"},
    "Imran": {"Wasim", "Faras"},
    "Faras": {"Imran"},
    "Mike": {"Amin"},
    "Nick": {"Amin"},
}

print(DFS(graph, "Amin"))
