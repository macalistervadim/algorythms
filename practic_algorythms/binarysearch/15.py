"""
Практика по алгоритму бинарного поиска, день 15
"""


class NumberNotFoundInList(ValueError):
    pass

def binary_search(numbers, target):
    low_element_index = 0
    high_element_index = len(numbers) - 1

    while low_element_index <= high_element_index:
        middle_element_index = (low_element_index+high_element_index) // 2
        gues_number = numbers[middle_element_index]

        if gues_number == target:
            return middle_element_index
        elif gues_number < target:
            low_element_index = middle_element_index + 1
        else:
            high_element_index = middle_element_index - 1

    raise NumberNotFoundInList(f"Number {target} not found in given numbers")


print(binary_search([1,2,3,4,5,6,7,8,9], 10))