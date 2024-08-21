"""
Практика по алгоритму сортировки пузырьком, день 8
"""

from typing import MutableSequence


def bubbleSort(numbers: MutableSequence[int]) -> MutableSequence[int]:
    highNumberIndex = len(numbers) - 1
    for i in range(highNumberIndex, 0, -1):
        reversed = False
        for j in range(i):
            if numbers[j] >= numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                reversed = True

        if not reversed:
            break

    return numbers


print(bubbleSort([1, 10, 9, 22, 4, 5, 2, 7]))
