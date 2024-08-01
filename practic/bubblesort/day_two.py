"""
Практика по Алгоритму Сортировки пузырьком, день 2
"""

from typing import MutableSequence, TypeVar


T = TypeVar('T')


def bubbleSort(nums: MutableSequence[T]) -> MutableSequence[T]:
    highElement: int = len(nums) - 1
    for i in range(highElement, 0, -1):
        mutable = False
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
                mutable = True

        if not mutable:
            break

    return nums


print(bubbleSort([5, 3, 2, 6, 9, 7, 1]))
