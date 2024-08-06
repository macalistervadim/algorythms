"""
Практика по алгоритму быстрой сортировки, день 3
"""


def quickSort(numbers):
    if len(numbers) < 2:
        return numbers
    
    middleIndex = len(numbers) // 2
    pivot = numbers[middleIndex]

    upperPivot = [i for i in numbers if i > pivot]
    lowerPivot = [i for i in numbers if i < pivot]
    equalsPivot = [i for i in numbers if i == pivot]

    return quickSort(lowerPivot) + equalsPivot + quickSort(upperPivot)


print(quickSort([8, 9, 6, 7, 2, 4, 3, 1]))