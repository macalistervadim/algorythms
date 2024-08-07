"""
Практика по алгоритму сортировки Шелла, день 1
"""


def shellSort(numbers):
    distance = len(numbers)//2

    while distance > 0:
        for i in range(distance, len(numbers)):
            temp = numbers[i]
            j = i

            while j >= distance and numbers[j - distance] > temp:
                numbers[j] = numbers[j - distance]
                j -= distance

            numbers[j] = temp

        distance //= 2

    return numbers


print(shellSort([7, 9, 8, 5, 1, 4, 3, 2]))
