"""
Практика по Алгоритму Сортировки Вставками, день 1
"""

from typing import MutableSequence


def insertionSort(numbers: MutableSequence[int]) -> MutableSequence[int]:
    for i in range(1, len(numbers)):
        j = i - 1
        elementNext = numbers[i]

        while j >= 0 and elementNext < numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1

        numbers[j + 1] = elementNext

    return numbers


print(insertionSort([5, 3, 6, 8, 2, 1]))