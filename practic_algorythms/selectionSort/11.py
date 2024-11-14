"""
Практика по алгоритму сортировки выбором, день 11
"""


def find_smallest(numbers):
    smallest = numbers[0]
    smallest_index = 0

    for i in range(1, len(numbers)):
        if numbers[i] < smallest:
            smallest = numbers[i]
            smallest_index = i

    return smallest_index

def selection_sort(numbers):
    new_list = []
    for i in range(len(numbers)):
        smallest = find_smallest(numbers)
        new_list.append(numbers.pop(smallest))

    return new_list


print(selection_sort([3, 2, 4, 5, 6, 7, 8, 100, 40, -1, -100, 9, 10]))