"""
практика по алгоритму сортировки выбором, день 14
"""


def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0

    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index

def selection_sort(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))

    return new_arr

print(selection_sort([10, 23, 6, 1293, 5,2, 6, -1]))
