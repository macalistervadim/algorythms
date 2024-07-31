"""
Тестирование алгоритма быстрой сортировки
"""

import array


def quicksort(nums: array.array[int]) -> array.array[int]:
    if len(nums) < 2:
        return nums
    else:
        # Выбор среднего элемента в качестве опорного
        middle_index = len(nums) // 2
        pivot = nums[middle_index]

        # Создаем массив чисел, меньше опорного элемента
        less = array.array(nums.typecode, [i for i in nums if i < pivot])

        # Создаем массив чисел, равных опорному элементу
        equal = array.array(nums.typecode, [i for i in nums if i == pivot])

        # Создаем массив чисел, больше опорного элемента
        greater = array.array(nums.typecode, [i for i in nums if i > pivot])

        return quicksort(less) + equal + quicksort(greater)


nums = array.array('i', [10, 5, 2, 3])
print(quicksort(nums))
