"""
Практика по алгориму бинарного поиска, день 7
"""


def quickSort(numbers):
    if len(numbers) < 2:
        return numbers
    
    middleElement = len(numbers) // 2
    pivot = numbers[middleElement]

    upperPivot = [i for i in numbers if i > pivot]
    lowerpivot = [i for i in numbers if i < pivot]
    equalPivot = [i for i in numbers if i == pivot]

    return quickSort(lowerpivot) + equalPivot + quickSort(upperPivot)


class NumberTargetNotFound(ValueError):
    """Value not found in numbers"""


def binarySearch(numbers, target):
    sortedNumbers = quickSort(numbers)

    lowElementIndex = 0
    highElementIndex = len(sortedNumbers) - 1

    while lowElementIndex < highElementIndex:
        middleElementIndex = (lowElementIndex+highElementIndex) // 2
        guesElement = sortedNumbers[middleElementIndex]

        if guesElement == target:
            return middleElementIndex
        elif guesElement > target:
            highElementIndex -= 1
        else:
            lowElementIndex += 1
    
    raise NumberTargetNotFound(f"Target {target} not found in numbers")


print(binarySearch([3, 6, 8, 1, 4, 2, 6, 9, 10], 11))