"""
Практика по алгоритму сортировки вставками, день 3
"""


def insertionSort(numbers):
    for i in range(1, len(numbers)):
        j = i-1
        elementNext = numbers[i]

        while j >= 0 and numbers[j] > elementNext:
            numbers[j+1] = numbers[j]
            j -= 1

        numbers[j+1] = elementNext
    
    return numbers


print(insertionSort([7, 9, 8, 1, 4, 5, 2, 3]))