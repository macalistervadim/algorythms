"""
Практика по алгоритму сортировки выбором, день 4
"""


def selectionSort(numbers):
    highElementIndex = len(numbers) - 1
    for i in range(highElementIndex, 0, -1):
        maxElement = 0
        for j in range(1, i+1):
            if numbers[j] > numbers[maxElement]:
                maxElement = j

        numbers[i], numbers[maxElement] = numbers[maxElement], numbers[i]

    return numbers


print(selectionSort([8, 4, 6, 1, 9, 3, 4]))