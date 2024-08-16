"""
Практика по алгортму быстрой сортировки, день 6
"""


def quickSort(numbers):
    if len(numbers) < 2:
        return numbers
    
    middleElement = len(numbers) // 2
    pivot = numbers[middleElement]

    uppersPivot = [i for i in numbers if i > pivot]
    lowersPivot = [i for i in numbers if i < pivot]
    equalsPivot = [i for i in numbers if i == pivot]

    return quickSort(lowersPivot) + equalsPivot + quickSort(uppersPivot)


print(quickSort([6, 9, 10, 5, 3, 6, 2 ,7]))
