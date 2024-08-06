"""
Практика по алгоритму Бинарного поиска, день 3
"""

from typing import MutableSequence


def binarySearch(nums: MutableSequence[float], tagret: float) -> float | None:
    lowIndex: int = 0
    highIndex: int = len(nums) - 1

    while lowIndex <= highIndex:
        middleIndex: int = (lowIndex + highIndex) // 2
        guestTarget = nums[middleIndex]

        if guestTarget == tagret:
            return middleIndex
        elif guestTarget > tagret:
            highIndex -= 1
        else:
            lowIndex += 1


print(binarySearch([1, 2, 5, 7, 9], 2))
