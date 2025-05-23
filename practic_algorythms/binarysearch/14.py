"""
Практика по алгоритму бинарного поиска, день 14
"""

class NotFindThisNumber(ValueError):
    pass

def binary_search(numbers, target):
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

    raise NotFindThisNumber(f"Number {target} not found in numbers")


print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 9))