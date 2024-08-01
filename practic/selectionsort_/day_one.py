"""
Практика по Алгоритму Сортировки Выбором, день 1
"""

from typing import MutableSequence


def findSmallNumber(nums: MutableSequence[int]) -> int:
    smallNumber = nums[0]
    smallIndex = 0
    for i in range(1, len(nums)):
        if nums[i] < smallNumber:
            smallNumber = nums[i]
            smallIndex = i
    
    return smallIndex


def selectionSort(nums: MutableSequence[int]) -> MutableSequence[int]:
    newNumsCollection: MutableSequence[int] = []
    for i in range(len(nums)):
        smallNumber = findSmallNumber(nums)
        newNumsCollection.append(nums.pop(smallNumber))
    
    return newNumsCollection

print(selectionSort([5, 3, 4, 2, 1, 8, 6, 9]))