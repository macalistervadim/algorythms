"""
практика по алгоритму сортировки выбором, день 13
"""

from typing import MutableSequence


def smallest_element(arr: MutableSequence[int]) -> int:
    smallest_index = 0
    smallest = arr[0]

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index

def selection_sort(arr: MutableSequence[int]) -> list[int]:
    result: list[int] = []

    for i in range(len(arr)):
        smallest = smallest_element(arr)
        result.append(arr.pop(smallest))
    
    return result

print(selection_sort([5, 3, 2, 4, 1]))