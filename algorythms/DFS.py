"""
Алгоритм поиска в глубину
"""

graph = {
    "Amin": {"Wasim", "Nick", "Mike"},
    "Wasim": {"Imran", "Amin"},
    "Imran": {"Wasim", "Faras"},
    "Faras": {"Imran"},
    "Mike": {"Amin"},
    "Nick": {"Amin"},
}


def DFS(graph, start, visited=None):
    if visited is None:
        visited = set()

    visited.add(start)
    print(start)
    for next in graph[start] - visited:
        DFS(graph, next, visited)

    return visited


print(DFS(graph, "Amin"))
