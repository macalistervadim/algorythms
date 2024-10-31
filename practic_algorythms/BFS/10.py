def BFS(graph, start_dot):
    visited = []
    queue = [start_dot]

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
