"""
Практика по алгоритму поиска в ширину (BFS)
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
    quque = [startDot]

    while quque:
        deleted = quque.pop(0)
        if deleted not in visited:
            visited.append(deleted)
            neigboursDeleted = graph[deleted]
            for neigbour in neigboursDeleted:
                quque.append(neigbour)
    
    return visited

