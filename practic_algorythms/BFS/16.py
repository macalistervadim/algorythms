"""
Практика по алгоритму поска в ширину, день 16
"""

def bfs(graph, start_dot):
    visited = []
    queue = [start_dot]

    while queue:
        this = queue.pop(0)
        if this not in visited:
            visited.append(this)

            neighbours = graph[this]
            queue.extend(neighbours)
            
    return visited

graph = {
    "Amin": {"Wasim", "Nick", "Mike"},
    "Wasim": {"Imran", "Amin"},
    "Imran": {"Wasim", "Faras"},
    "Faras": {"Imran"},
    "Mike": {"Amin"},
    "Nick": {"Amin"},
}

print(bfs(graph, "Amin"))
