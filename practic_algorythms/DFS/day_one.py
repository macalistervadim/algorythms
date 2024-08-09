"""
Практика по алгоритму поиска в глубину (DFS)
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

    for nextNeighbour in graph[startDot] - visited:
        DFS(graph, nextNeighbour, visited)
    
    return visited


print(DFS(graph, "Amin"))