"""
Практика по алгоритму поиска в ширину
"""


graph = {
    "Amin": {"Wasim", "Nick", "Mike"},
    "Wasim": {"Imran", "Amin"},
    "Imran": {"Wasim", "Faras"},
    "Faras": {"Imran"},
    "Mike": {"Amin"},
    "Nick": {"Amin"},
}


def BFS(graph, startDot):
    visited = []
    queue = [startDot]

    while queue:
        target = queue.pop(0)
        if target not in visited:
            visited.append(target)
            neighbours = graph[target]
            for neighbour in neighbours:
                queue.append(neighbour)

    return visited


print(BFS(graph, "Amin"))
