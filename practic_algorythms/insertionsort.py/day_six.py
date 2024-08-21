"""
Практика по алгоритму сортировки вставками, день 6
"""

from typing import MutableSequence


def insertionSort(numbers: MutableSequence[int]) -> MutableSequence[int]:
    for i in range(1, len(numbers)):
        j = i - 1
        elementNext = numbers[i]

        while j >= 0 and numbers[j] >= elementNext:
            numbers[j+1] = numbers[j]
            j -= 1

        numbers[j+1] = elementNext

    return numbers


print(insertionSort([5, 10, 22, 4, 5, 2, 1]))
