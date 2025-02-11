"""
Практика по алгоритму бинарного поиска, день 23
"""

def binary_search(arr: list[int], target: int) -> int:
    low_number_index = 0
    high_number_index = len(arr) - 1
    
    while low_number_index <= high_number_index:
        middle_number_index = (low_number_index + high_number_index) // 2
        gues_number = arr[middle_number_index]
        
        if gues_number == target:
            return middle_number_index
        elif gues_number > target:
            high_number_index = middle_number_index - 1
        else:
            low_number_index = middle_number_index + 1
    return -1

print(binary_search([1, 3, 5, 7, 9, 10, 20, 22], 3))