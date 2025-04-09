"""
Дан массив nums, содержащий n различных чисел в диапазоне [0, n].
Необходимо вернуть единственное число из диапазона, которого не хватает в массиве.
"""

def missing_number(nums: list[int]) -> int:
    for i in range(len(nums)+1):
        if i not in nums:
            return i
        

missing_number([9,6,4,2,3,5,7,0,1])

# Time complexity: O(n)
# Space complexity: O(1)