"""
Практика по алгоритму быстрой сортировки, день 15
"""


def quick_sort(numbers):
    if len(numbers) < 2:
        return numbers
    else:
        pivot = numbers[len(numbers) // 2]
        
        left = [i for i in numbers if i < pivot]
        middle = [i for i in numbers if i == pivot]
        right = [i for i in numbers if i > pivot]
        
        return quick_sort(left) + middle + quick_sort(right)
    
    
print(quick_sort([10, 5, 2, 3]))