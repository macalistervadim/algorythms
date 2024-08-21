"""
Практика по алгоритму сортировки выбором, день 8
"""

from typing import MutableSequence


def selectionSort(numbers: MutableSequence[int]) -> MutableSequence[int]:
    highElementIndex = len(numbers) - 1
    for i in range(highElementIndex, 0, -1):
        maxElementIndex = 0
        for j in range(1, i + 1):
            if numbers[j] > numbers[maxElementIndex]:
                maxElementIndex = j

        numbers[i], numbers[maxElementIndex] = \
            numbers[maxElementIndex], numbers[i]

    return numbers


print(selectionSort([10, 2, 9, 8, 50, 22, 1]))
