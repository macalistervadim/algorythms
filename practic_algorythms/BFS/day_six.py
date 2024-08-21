"""
Практика по алгоритму поиска в ширину, день 6
"""

from typing import Mapping, MutableSequence


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
    startDot: str
) -> MutableSequence[str]:
    visited: MutableSequence[str] = []
    queue: MutableSequence[str] = [startDot]

    while queue:
        this = queue.pop(0)
        if this not in visited:
            visited.append(this)

            neighbours = graph[this]
            for neighbour in neighbours:
                queue.append(neighbour)

    return visited


print(BFS(graph, "Amin"))
