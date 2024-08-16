"""
Практика по алгоритму сортировки пузрьком, день 6
"""


def bubbleSort(numbers):
    highElementIndex = len(numbers) - 1
    for i in range(highElementIndex, 0, -1):
        swapped = False
        for j in range(i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                swapped = True

        if not swapped:
            break
    
    return numbers

print(bubbleSort([5, 7, 9, 10, 2, 3, 4, 9]))