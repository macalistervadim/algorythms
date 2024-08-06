"""
повторение Алгоритма Бинарного поиска день 2
"""

from typing import MutableSequence


def binarySearch(nums: MutableSequence[float], target: int) -> int:
    low = 0
    high = len(nums) - 1

    while low <= high:
        middle = (low+high) // 2
        guest = nums[middle]

        if guest == target:
            return middle
        elif guest > target:
            high -= 1
        else:
            low += 1

    return 0


print(binarySearch([1, 5, 10, 15], 10))
