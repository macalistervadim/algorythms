"""
Практика по алгоритму сортировки выбором, день 10
"""

from typing import MutableSequence


def find_smallest(arr: MutableSequence[int]) -> int:
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index


def selection_sort(arr: MutableSequence[int]) -> MutableSequence[int]:
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))

    return new_arr


print(selection_sort([100, 39, 2, 0, 9, 5, 1, 8]))

