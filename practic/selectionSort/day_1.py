"""
Практика по алгоритму сортировки выбором, день 1
"""


def findSmallest(nums: list[int]) -> int:
    smallest = nums[0]
    smallest_index = 0
    for i in range(1, len(nums)):
        if nums[i] < smallest:
            smallest = nums[i]
            smallest_index = i

    return smallest_index


def selectionSort(nums: list[int]) -> list[int]:
    newNums: list[int] = []
    for i in range(len(nums)):
        smallest = findSmallest(nums)
        newNums.append(nums.pop(smallest))

    return newNums


print(selectionSort([6, 1, 10, 3, 9, 5]))
