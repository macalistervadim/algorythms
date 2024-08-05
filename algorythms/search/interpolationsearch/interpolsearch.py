"""
Алгоритм Интерполяционный поиск

Основная суть и отличие от бинарного поиска в том, что мы не просто
"делим пополам" наш массив, с ищем на основе нашего таргета его позицию
в том месте, где нужно. Тоесть формула предполагает факт, что допустим
число должно быть левее середины - тогда поиск будет проходить там.
Опять же из минусов - работает только с отсортированными данными 
"""


def interpolationSearch(array, target):
    idx0 = 0
    idxn = (len(array) - 1)
    found = False

    while idx0 <= idxn and target >= array[idx0] and target <= array[idxn]:
        # Ищем среднюю точку
        middle = idx0 + int(((float(idxn - idx0) / (array[idxn] - array[idx0])) * (target - array[idx0])))
        
        # Сравниваем значение в средней точке со значением поиска
        if array[middle] == target:
            return True
        elif array[middle] < target:
            idx0 = middle + 1
        else:
            idxn = middle - 1
    
    return found


lst = [1, 2, 4, 6, 7, 9, 10, 14, 17]
print(interpolationSearch(lst, 1))

