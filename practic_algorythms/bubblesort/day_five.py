"""
Практика по алгоритму сортировки пузырьком
"""


def bubbleSort(numbers):
    highElementIndex = len(numbers) - 1
    for i in range(highElementIndex, 0, -1):
        mutable = False
        for j in range(i):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                mutable = True

        if not mutable:
            break
    
    return numbers


print(bubbleSort([4, 7, 9, 1, 5, 7, 2, 4, 3]))