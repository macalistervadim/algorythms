"""
Практика по алгоритму сортвроки в ширину, день 5
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
        this = queue.pop(0)
        if this not in visited:
            visited.append(this)
            neighbours = graph[this]

            for neighbour in neighbours:
                queue.append(neighbour)
        
    return visited

print(BFS(graph, "Amin"))