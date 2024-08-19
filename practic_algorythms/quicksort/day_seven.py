"""
Практика по алгоритму быстрой сортирвоки, день 7
"""


def quickSort(numbers: list[int]) -> list[int]:
    if len(numbers) < 2:
        return numbers

    middleElementIndex = len(numbers) // 2
    pivot = numbers[middleElementIndex]

    upperPivotElements: list[int] = (
        [i for i in numbers if i > pivot])
    lowerPivotElements: list[int] = (
        [i for i in numbers if i < pivot])
    equalsPivotElements: list[int] = (
        [i for i in numbers if i == pivot])

    return (
        quickSort(lowerPivotElements) +
        equalsPivotElements +
        quickSort(upperPivotElements)
    )


print(quickSort([10, 9, 2, 4, 5, 11, 20, 23]))
