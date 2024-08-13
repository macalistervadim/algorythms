"""
Практика по алгоритму быстрой сортировки, день 5
"""


def quickSort(numbers):
    if len(numbers) < 2:
        return numbers

    middleElementIndex = len(numbers) // 2
    pivot = numbers[middleElementIndex]

    lowerPivotElements = [i for i in numbers if i < pivot]
    upperPivotElements = [i for i in numbers if i > pivot]
    equalsPivotElements = [i for i in numbers if i == pivot]

    return (
        quickSort(lowerPivotElements) +
        equalsPivotElements +
        quickSort(upperPivotElements)
    )

print(quickSort([6, 8, 9, 1, 4, 3, 2, 5]))