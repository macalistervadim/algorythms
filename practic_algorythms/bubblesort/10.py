"""
Практика по алгоритму сортировки пузырьком, день 10
"""

def bubble_sort(arr: list[int]):
    high_number_index = len(arr) - 1
    for i in range(high_number_index, 0, -1):
        reversed = False
        for j in range(i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                reversed = True
        
        if not reversed:
            break
    
    return arr

print(bubble_sort([20, 10, -1, 2095, 218, 2]))