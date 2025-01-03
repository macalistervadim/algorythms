"""
практика по алгоритму быстрой сортировки, день 12
"""


def quick_sort(numbers):
    if len(numbers) < 2:
        return numbers
    else:
        pivot = numbers[len(numbers) // 2]

        left = [i for i in numbers if i < pivot]
        right = [i for i in numbers if i > pivot]
        equal = [i for i in numbers if i == pivot]

        return quick_sort(left) + equal + quick_sort(right)


print(quick_sort([5, 4, 3, 2, 1]))
