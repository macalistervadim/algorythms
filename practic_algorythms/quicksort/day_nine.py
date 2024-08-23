"""
Практика по алгоритму быстрой сортировки, день 9
"""


def quickSort(numbers: list[int]) -> list[int]:
    if len(numbers) < 2:
        return numbers

    middleElementIndex = len(numbers) // 2
    pivotNumber = numbers[middleElementIndex]

    upperPivotNumbers = [i for i in numbers if i > pivotNumber]
    lowerPivotNumbers = [i for i in numbers if i < pivotNumber]
    equalPivotNumbers = [i for i in numbers if i == pivotNumber]

    return (
        quickSort(lowerPivotNumbers) +
        equalPivotNumbers +
        quickSort(upperPivotNumbers)
    )


print(quickSort([10, 4, 20, 99, 3, 3, 3, 5, 8, 1]))
