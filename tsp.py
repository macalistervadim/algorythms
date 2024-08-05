"""
Практическое решение задачи о коммивояжере при помощи стратегии
"Жадного алгоритма". Тобишь данное решение не является
глобально верным, но является оптимальным и быстрым
"""

import math


# Функция для вычисления расстояния между двумя точками
def distance_points(a, b):
    # Предположим, что точки a и b являются кортежами (x, y)
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)


def greedyAlgorythm(cities, start=None):
    c = start or first(cities)
    tour = [c]
    unvisited = set(cities) - {c}
    while unvisited:
        c = nearest_neighbor(c, unvisited)
        tour.append(c)
        unvisited.remove(c)
    return tour


def first(collection):
    return next(iter(collection))


def nearest_neighbor(a, cities):
    return min(cities, key=lambda c: distance_points(c, a))


cities = {(0, 0), (1, 5), (4, 2), (6, 6), (3, 8)}
start_point = (0, 0)
tour = greedyAlgorythm(cities, start_point)

print("Порядок посещения городов:", tour)
