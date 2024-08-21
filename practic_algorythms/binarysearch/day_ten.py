"""
Практика по алгоритму бинарного поиска, день 10
"""

from typing import MutableSequence


class ValueNotFoundInNumbers(ValueError):
    """Value not found in numbers"""
    pass


def binarySearch(
    numbers: MutableSequence[int],
    targetNumber: int
) -> int:
    lowNumberIndex = 0
    highNumberIndex = len(numbers)-1

    while lowNumberIndex <= highNumberIndex:
        middleNumberIndex = (lowNumberIndex+highNumberIndex)//2
        guesNumber = numbers[middleNumberIndex]

        if guesNumber == targetNumber:
            return middleNumberIndex
        elif guesNumber > targetNumber:
            highNumberIndex -= 1
        else:
            lowNumberIndex += 1

    raise ValueNotFoundInNumbers(f"Target {targetNumber} not found.")


print(binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9], 9))
