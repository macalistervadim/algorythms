"""
Тестирование алгоритма сортировки выбором
"""

from typing import List, Union


def findSmallest(arr: List[Union[int, float]]) -> Union[int, float]:
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


def selectionSort(arr: List[Union[int, float]]) -> List[Union[int, float]]:
    newArr: List[Union[int, float]] = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
    return newArr

print(selectionSort([5.1, 3.3, 6, 2, 10]))