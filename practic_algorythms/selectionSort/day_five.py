"""
Практика по алгоритму сортировки вставками, день 5
"""


def selectionSort(numbers):
    highElementIndex = len(numbers) - 1
    for i in range(highElementIndex, 0, -1):
        maxElementIndex = 0
        for j in range(1, i+1):
            if numbers[j] > numbers[maxElementIndex]:
                maxElementIndex = j
        
        numbers[j], numbers[maxElementIndex] = numbers[maxElementIndex], numbers[j] 

    return numbers


print(selectionSort([5, 7, 9, 12, 3, 4, 5, 2, 4]))