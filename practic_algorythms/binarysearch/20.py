"""
практика по алгоритму бинарного поиска день 20
"""


def binary_search(numbers, target):
    low_number_index = 0
    high_number_index = len(numbers) - 1

    while low_number_index <= high_number_index:
        middle_number_index = (low_number_index + high_number_index) // 2
        gues_number = numbers[middle_number_index]

        if gues_number == target:
            return middle_number_index
        elif gues_number > target:
            high_number_index = middle_number_index - 1
        else:
            low_number_index = middle_number_index + 1

    return -1

print(binary_search([1, 2, 10, 20, 100, 1000], 1000000))