"""
повторение Алгоритма Пузырьковой сортировки день 1
"""

from typing import MutableSequence, TypeVar

T = TypeVar("T")


def bubbleSort(nums: MutableSequence[T]) -> MutableSequence[T]:
    highElement = len(nums) - 1
    for i in range(highElement, 0, -1):
        swapped = False
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]

                swapped = True

        if not swapped:
            break

    return nums


print(bubbleSort([5, 1, 4, 2, 3, 10, 9, 7]))
