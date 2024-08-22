"""
Пракитка по алгоритму бинарного поиска, день 11
"""

from typing import MutableSequence


class NotFoundThisTarget(ValueError):
    """Not found this target in numbers"""
    pass


def binarySearch(numbers: MutableSequence[int], target: int) -> int:
    lowNumberIndex = 0
    highNumberIndex = len(numbers) - 1

    while lowNumberIndex <= highNumberIndex:
        middleNumberIndex = (lowNumberIndex + highNumberIndex) // 2
        guesNumber = numbers[middleNumberIndex]

        if guesNumber == target:
            return middleNumberIndex
        elif guesNumber > target:
            highNumberIndex -= 1
        else:
            lowNumberIndex += 1

    raise NotFoundThisTarget(f"Not found target={target} in numbers")


print(binarySearch([1, 3, 4, 5, 6, 7, 8, 10], 11))
