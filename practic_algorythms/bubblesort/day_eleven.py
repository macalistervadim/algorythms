"""
Практика по алгоритму сортировки пузырьком, день 10
"""

from typing import MutableSequence


def bubble_sort(numbers: MutableSequence[int]) -> MutableSequence[int]:
    high_element_index = len(numbers) - 1
    for i in range(high_element_index, 0, -1):
        swapped = False
        for j in range(i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                swapped = True

        if not swapped:
            break

    return numbers


print(bubble_sort([10, 2, 100, -20, 3, -1_000_000]))