"""
Практика по алгоритму спортировки выбором, день 9
"""

from typing import MutableSequence


def selectionSort(numbers: MutableSequence[int]) -> MutableSequence[int]:
    highElementIndex = len(numbers) - 1
    for i in range(highElementIndex, 0, -1):
        maxIndex = 0
        for j in range(1, i+1):
            if numbers[j] > numbers[maxIndex]:
                maxIndex = j

        numbers[i], numbers[maxIndex] = numbers[maxIndex], numbers[j]

    return numbers


print(selectionSort([10, 9, 22, 90, 4, 5, 1]))
