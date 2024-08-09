"""
Практика по алгоритму быстрой сортировки
"""


def quickSort(numbers):
    if len(numbers) < 2:
        return numbers
    
    middleElement = len(numbers) // 2
    pivot = numbers[middleElement]

    upperNumbersPivot = [i for i in numbers if i > pivot]
    lowestNumbersPivot = [i for i in numbers if i < pivot]
    equalsNumbersPivot = [i for i in numbers if i == pivot]

    return quickSort(lowestNumbersPivot) + equalsNumbersPivot + quickSort(upperNumbersPivot)


print(quickSort([7, 9, 5, 8, 1, 5, 4, 2, 3]))