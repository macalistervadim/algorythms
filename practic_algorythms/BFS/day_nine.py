"""
Практика по алгоритму поиска в ширину, день 9
"""

from typing import Mapping, MutableSequence


def BFS(
    graph: Mapping[str, set[str]],
    start_dot: str
) -> MutableSequence[str]:
    visited: MutableSequence[str] = []
    queue: MutableSequence[str] = [start_dot]

    while queue:
        this = queue.pop(0)
        if this not in visited:
            visited.append(this)

            neighbours = graph[this]
            for neighbour in neighbours:
                queue.append(neighbour)

    return visited


graph = {
    "Amin": {"Wasim", "Nick", "Mike"},
    "Wasim": {"Imran", "Amin"},
    "Imran": {"Wasim", "Faras"},
    "Faras": {"Imran"},
    "Mike": {"Amin"},
    "Nick": {"Amin"},
}


print(BFS(graph, "Amin"))
