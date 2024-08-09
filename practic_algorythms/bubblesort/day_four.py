"""
Практика по алгортиму сортировки пузырьком, день 4
"""


def bubbleSort(numbers):
    highElement = len(numbers) - 1
    for i in range(highElement, 0, -1):
        swapped = False
        for j in range(i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                swapped = True

        if not swapped:
            break

    return numbers


print(bubbleSort([6, 7, 8, 4, 5, 1, 3, 2]))
