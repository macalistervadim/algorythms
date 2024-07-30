"""
Алгоритм Сортировки Пузырьком
"""

from typing import TypeVar, MutableSequence

T = TypeVar("T")


def bubbleSort(list_: MutableSequence[T]) -> MutableSequence[T]:
    lastElem = len(list_) - 1
    for passNo in range(lastElem, 0, -1):
        swapped = False
        for i in range(passNo):
            if list_[i] > list_[i+1]:
                list_[i], list_[i+1] = list_[i+1], list_[i]
                swapped = True

        if not swapped:
            break

    return list_


print(bubbleSort([4, 1, 2, 5, 10, 7]))
