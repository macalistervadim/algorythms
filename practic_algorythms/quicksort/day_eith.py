"""
Практика по алгоритму быстрой сортировки, день 8
"""


def quickSort(numbers: list[int]) -> list[int]:
    if len(numbers) < 2:
        return numbers

    middleElementIndex = len(numbers) // 2
    pivot = numbers[middleElementIndex]

    upperPivotElements = [i for i in numbers if i > pivot]
    lowerPivotElements = [i for i in numbers if i < pivot]
    equalsPivotElements = [i for i in numbers if i == pivot]

    return (
        quickSort(lowerPivotElements) +
        equalsPivotElements +
        quickSort(upperPivotElements)
    )


print(quickSort([10, 22, 4, 7, 2, 1, 50]))
