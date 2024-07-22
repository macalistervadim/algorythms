"""
Повторение алгоритма бинарного поиска день 1
"""


def binarySearch(nums: list[int], target: int) -> int:
    low = 0 
    high = len(nums) - 1

    while low <= high:
        middle = (low + high) // 2
        print(middle)
        gues = nums[middle]

        if gues == target:
            return middle
        elif gues > target:
            high -= 1
        else:
            low += 1

    return 0


print(binarySearch([1, 5, 10, 15, 40, 100], 40))
