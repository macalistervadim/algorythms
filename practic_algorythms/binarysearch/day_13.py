"""
Практика по алгоритму бинарного поиска, день 13
"""

from typing import MutableSequence


def binary_search(
    numbers: MutableSequence[int],
    target_number: int
) -> int:
    """
    this function returned target value but find it.
    """
    low_number_index = 0
    high_number_index = len(numbers) - 1

    while low_number_index <= high_number_index:
        middle_number_index = (low_number_index + high_number_index) // 2
        gues_number = numbers[middle_number_index]

        if gues_number == target_number:
            return middle_number_index
        elif gues_number > target_number:
            high_number_index -= 1
        else:
            low_number_index += 1

    return -1




print(binary_search([1, 2, 3, 10, 22, 100, 1000], 3))

####### # 3 3 3dsfsdfsdfsdfsdfsdf
"""
sdfsdfsdf
"""