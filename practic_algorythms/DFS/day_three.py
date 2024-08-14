"""
Практика по алгоритму поиска в глубину, день 3
"""

graph = {
    "Amin": {"Wasim", "Nick", "Mike"},
    "Wasim": {"Imran", "Amin"},
    "Imran": {"Wasim", "Faras"},
    "Faras": {"Imran"},
    "Mike": {"Amin"},
    "Nick": {"Amin"},
}


def DFS(graph, startDot, visited=None):
    if not visited:
        visited = set()

    visited.add(startDot)

    for i in graph[startDot] - visited:
        DFS(graph, i, visited)

    return visited


print(DFS(graph, "Amin"))