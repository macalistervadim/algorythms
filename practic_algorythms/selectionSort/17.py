"""
Практика по алгоритму сортировки выбором, день 17
"""

def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    
    for i in range(len(arr) - 1):
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

print(selection_sort([5, 3, 6, 2, 10]))