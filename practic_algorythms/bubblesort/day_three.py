"""
Практика по Алгоритму сортировки Пузярьком, день 3
"""


def bubbleSort(numbers):
    for i in range(len(numbers) - 1, 0, -1):
        sorted = False
        for j in range(i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                sorted = True
        
        if not sorted:
            break

    return numbers


print(bubbleSort([7, 5, 6, 4, 5, 3, 1, 2]))