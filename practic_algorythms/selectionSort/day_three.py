"""
Практика по алгоритму сортировки выбором, день 3
"""


def selectionSort(numbers):
    for i in range(len(numbers) - 1, 0, -1):
        max_index = 0
        for j in range(1, i + 1):
            if numbers[j] > numbers[max_index]:
                max_index = j

        numbers[i], numbers[max_index] = numbers[max_index], numbers[i]

    return numbers


print(selectionSort([8, 6, 7, 5, 6, 4, 1, 3, 2]))
