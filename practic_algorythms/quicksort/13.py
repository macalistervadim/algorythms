"""
практика по алгоритму быстрой сортировки, день 13
"""


def quick_sort(numbers):
    if len(numbers) < 2:
        return numbers
    else:
        pivot = numbers[len(numbers) // 2]

        lower_pivot = [i for i in numbers if i < pivot]
        upper_pivot = [i for i in numbers if i > pivot]
        equals_pivot = [i for i in numbers if i == pivot]

        return quick_sort(lower_pivot) + equals_pivot + quick_sort(upper_pivot)

print(quick_sort([10, 2, -1, 100, 239, -321, 23]))