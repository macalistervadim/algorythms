"""
Практика по алгоритму сортировки вставками, день 5
"""


def insertionSort(numbers):
    for i in range(1, len(numbers)):
        j = i - 1
        elementNext = numbers[i]

        while j >= 0 and numbers[j] > elementNext:
            numbers[j+1] = numbers[j]
            j -= 1
    
        numbers[j+1] = elementNext

    return numbers

print(insertionSort([2, 5, 7,9, 1, 4, 6, 2, 7, 8]))