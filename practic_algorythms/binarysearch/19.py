"""
практика по алгоритму бинарного поиска, день 19
"""


class NumberNotFound(ValueError):
    pass


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

    raise NumberNotFound(f"target number {target} not found")


print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 10))