"""
практика по алгоритму бинарного поиска, день 21
"""


def binary_search(numbers, target):
    low_num_index = 0
    high_num_index = len(numbers) - 1

    while low_num_index <= high_num_index:
        middle_num_index = (low_num_index + high_num_index) // 2
        gues_number = numbers[middle_num_index]

        if gues_number == target:
            return middle_num_index
        elif gues_number > target:
            high_num_index = middle_num_index - 1
        else:
            low_num_index = middle_num_index + 1

    return -1