"""
Практика алгоритма быстрой сортировки день 1
"""

import array


def quickSort(array_: array.array[int]) -> array.array[int]:
    if len(array_) < 2:
        return array_
    else:
        middle_index = len(array_) // 2
        pivot = array_[middle_index]

        upper = array.array('i', [i for i in array_ if i > pivot])
        self_ = array.array('i', [i for i in array_ if i == pivot])
        lower = array.array('i', [i for i in array_ if i < pivot])

        return quickSort(lower) + self_ + quickSort(upper)


print(quickSort(array.array('i', [5, 1, 10, 2, 6, 8])))
