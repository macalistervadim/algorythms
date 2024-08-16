"""
Практика по алгоритму сортировки в ширину, день 4
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
        thisDot = queue.pop(0)
        if thisDot not in visited:
            visited.append(thisDot)

            neighbours = graph[thisDot]
            for neighbour in neighbours:
                queue.append(neighbour)

    return visited

print(BFS(graph, "Amin"))