"""
Практика по алгоритму сортировки вставками, день 2
"""


def insertionSort(numbers):
    for i in range(1, len(numbers)):
        j = i - 1
        elemNext = numbers[i]

        while j >= 0 and numbers[j] > elemNext:
            numbers[j + 1] = numbers[j]
            j -= 1

        numbers[j+1] = elemNext

    return numbers


print(insertionSort([7, 5, 6, 8, 9, 1, 3, 2]))
