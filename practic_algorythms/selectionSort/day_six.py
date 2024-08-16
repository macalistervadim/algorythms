"""
Практика по алгортиму сортировки выбором, день 6
"""


def selectionSort(numbers):
    highElement = len(numbers) - 1
    for i in range(highElement, 0, -1):
        maxElement = 0
        for j in range(1, i+1):
            if numbers[j] > numbers[maxElement]:
                maxElement = j
        
        numbers[i], numbers[maxElement] = numbers[maxElement], numbers[j]

    return numbers


print(selectionSort([6, 8, 10 ,4, 5, 2, 7, 8]))