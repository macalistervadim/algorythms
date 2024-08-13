"""
Практика по алгоритму бинарного поиска, день 6
"""


class NoSearchElement(ValueError):
    """No search element"""


def binarySearch(numbers, targetNumber):
    lowElementIndex = 0
    highElementIndex = len(numbers) - 1

    while lowElementIndex <= highElementIndex:
        middleElementIndex = (
            (lowElementIndex+highElementIndex) // 2
        )
        guestNumber = numbers[middleElementIndex]

        if guestNumber == targetNumber:
            return middleElementIndex
        elif guestNumber > targetNumber:
            highElementIndex -= 1
        else:
            lowElementIndex += 1

    raise NoSearchElement("No search...")


print(binarySearch([1, 3, 5, 6, 7, 8, 9, 11, 14], 11))