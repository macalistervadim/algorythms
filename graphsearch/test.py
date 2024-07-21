"""
Алгоритм поиска в ширину
"""

import collections

graph = {}
graph["claire"] = ["thom", "jonny"]
graph["anuj"] = []
graph["you"] = ["claire", "anuj"]


def person_is_seller(name: str) -> bool:
    """
    Проверяем, является ли человек продавцом манго
    """
    return name.endswith("m")


def search(name: str) -> bool:
    search_queue = collections.deque()
    search_queue += graph[name]
    searched = []
    while search_queue:
        person = search_queue.popleft()
        if person not in searched:
            if person_is_seller(person):
                print(f"{person} продавец манго!")
                return True
            else:
                search_queue += graph[person]
                searched.append(person)
    return False


search("you")
