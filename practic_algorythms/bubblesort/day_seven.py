"""
Практика по алгоритму сортировки пузырьком, день 7
"""

from typing import MutableSequence


def bubbleSort(numbers: MutableSequence[int]) -> MutableSequence[int]:
    highElementIndex = len(numbers) - 1

    for i in range(highElementIndex, 0, -1):
        reversed = False
        for j in range(i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                reversed = True
        
        if not reversed:
            break

    return numbers

print(bubbleSort([5, 6, 9, 10, 4, 3, 22, 12]))