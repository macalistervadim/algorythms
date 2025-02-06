"""
Практика по алгоритму бинарного поиска, день 22
"""


def binary_search(numbers, target):
    low_number_index = 0
    high_number_index = len(numbers) - 1

    while low_number_index <= high_number_index:
        middle_number_index = (low_number_index + high_number_index) // 2
        gues_number = numbers[middle_number_index]

        if target == gues_number:
            return middle_number_index
        elif gues_number > target:
            high_number_index = middle_number_index - 1
        else:
            low_number_index = middle_number_index + 1

    return -1

print(binary_search([1, 3, 5, 6, 7, 8, 9, 11, 14], 11))
