"""
Практика по Алгоритму Быстрой сортировки, день 2


P.S - Здесь провел некое тестирование быстродействия. Оказалось что вариант с модулем array
конкретно в данном случае - проигрышный. Видимо дело в том, что для списков питон
ничего не делает особенного, просто вызывая конкструктор, а в массивах -
мы помимо самих списов еще и тащим за собой массивы. Крч массивы в данном случае - фуфло

Уверен что с большим объемом данных, массивы наверняка шустрее. Но тут не такой случай,
да и сам алгоритм не справится с большим объемом
"""

import array
import random
import time
import memory_profiler


# def quickSort(nums: array.array[int]) -> array.array[int]:
#     if len(nums) < 2:
#         return nums
#     else:
#         middleIndex = random.randrange(len(nums))
#         pivot = nums[middleIndex]
        
#         upperPivot = array.array("i", [num for num in nums if num > pivot])
#         lowerPivot = array.array("i", [num for num in nums if num < pivot])
#         equalsPivot = array.array("i", [num for num in nums if num == pivot])

#         return quickSort(lowerPivot) + equalsPivot + quickSort(upperPivot)

# @memory_profiler.profile
# def test_quickSort():
#     start_time = time.time()
#     result = quickSort(array.array('i', [4, 2, 1, 6, 9, 10, 7]))
#     print("Time taken:", time.time() - start_time)
#     return result


# # Запуск теста
# test_quickSort()


def quickSort(nums: list[int]) -> list[int]:
    if len(nums) < 2:
        return nums
    else:
        middleIndex = random.randrange(len(nums))
        pivot = nums[middleIndex]
        
        upperPivot = [num for num in nums if num > pivot]
        lowerPivot = [num for num in nums if num < pivot]
        equalsPivot = [num for num in nums if num == pivot]

        return quickSort(lowerPivot) + equalsPivot + quickSort(upperPivot)

@memory_profiler.profile
def test_quickSort():
    start_time = time.time()
    result = quickSort([4, 2, 1, 6, 9, 10, 7])
    print("Time taken:", time.time() - start_time)
    return result


# Запуск теста
test_quickSort()