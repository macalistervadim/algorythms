"""
Практика по алгоритму бинарного поиска, день 8
"""


class ThisTargetNotFound(ValueError):
    """This target not found in numbers."""
    pass


def binarySearch(numbers, target):
    lowNumberIndex = 0
    highNumberIndex = len(numbers) - 1

    while lowNumberIndex <= highNumberIndex:
        middleNumberIndex = (lowNumberIndex+highNumberIndex)//2
        guesNumber = numbers[middleNumberIndex]

        if guesNumber == target:
            return middleNumberIndex
        elif guesNumber > target:
            highNumberIndex -= 1
        else:
            lowNumberIndex += 1
        
    raise ThisTargetNotFound(f"Target {target} not found in numbers")


print(binarySearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10))