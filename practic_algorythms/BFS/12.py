"""
практика по алгоритму поиска в ширину, день 12
"""

graph = {
    "Amin": {"Wasim", "Nick", "Mike"},
    "Wasim": {"Imran", "Amin"},
    "Imran": {"Wasim", "Faras"},
    "Faras": {"Imran"},
    "Mike": {"Amin"},
    "Nick": {"Amin"},
}


def BFS(graphs, start_dot):
    visited = []
    queue = [start_dot]

    while queue:
        this = queue.pop(0)
        if this not in visited:
            visited.append(this)

            neighbours = graphs[this]
            for neighbour in neighbours:
               queue.append(neighbour)

    return visited


print(BFS(graph, "Amin"))
