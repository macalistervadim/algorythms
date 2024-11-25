"""
практика по алгоритму бинарного поиска, день 17
"""

from typing import MutableSequence


class NotFoundThisTarget(ValueError):
    pass


def binary_search(numbers: MutableSequence[int], target: int) -> int:
    low_number_index = 0
    high_number_index = len(numbers) - 1

    while low_number_index <= high_number_index:
        middle_number_index = (low_number_index + high_number_index) // 2
        gues_number = numbers[middle_number_index]

        if gues_number == target:
            return middle_number_index
        elif gues_number < target:
            low_number_index = middle_number_index + 1
        else:
            high_number_index = middle_number_index - 1

    raise NotFoundThisTarget(f"number {target} not found")


print(binary_search([1.019192, 2.21391, 3, 4, 5, 6, 7, 8, 9], 9))