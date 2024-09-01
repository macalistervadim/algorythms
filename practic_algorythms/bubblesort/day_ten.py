"""
Практика по алгоритму сортировки пузырьком, день 10
"""

from typing import MutableSequence


def bubbleSort(numbers: MutableSequence[int]) -> MutableSequence[int]:
    highNumberIndex = len(numbers) - 1
    for i in range(highNumberIndex, 0, -1):
        swapped = False
        for j in range(i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                swapped = True

        if not swapped:
            break

    return numbers


print(bubbleSort([10, 9, 20, 4, 7, 1]))
