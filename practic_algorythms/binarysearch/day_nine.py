"""
Практика по алгоритму бинарного поиска, день 9
"""

from typing import MutableSequence


def binarySearch(numbers: MutableSequence[int], target: int) -> str | int:
    lowElementIndex = 0
    highElementIndex = len(numbers) - 1

    while lowElementIndex <= highElementIndex:
        middleElementIndex = (lowElementIndex+highElementIndex) // 2
        guesNumber = numbers[middleElementIndex]

        if guesNumber == target:
            return middleElementIndex
        elif guesNumber > target:
            highElementIndex -= 1
        else:
            lowElementIndex += 1
    
    return "Not found this target"


print(binarySearch([1, 3, 4, 5, 6, 7, 8, 9], 9))