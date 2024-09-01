"""
Практика по алгоритму бинарного поиска, день 12
"""

from typing import MutableSequence


def binarySearch(numbers: MutableSequence, target: int) -> int:
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

    return -1


print(binarySearch([1, 4, 5, 6, 9, 10, 22], 4))
