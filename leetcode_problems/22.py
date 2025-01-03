"""
Implement a function signFunc(x) that returns:

1 if x is positive.
-1 if x is negative.
0 if x is equal to 0.
You are given an integer array nums. Let product be the product of all values in the array nums.

Return signFunc(product).
"""


def arraySign(nums: list[int]) -> int:
    sum = 1
    for i in nums:
        sum *= i

    if sum > 0:
        return 1
    elif sum < 0:
        return -1
    elif sum == 0:
        return 0

print(arraySign([-1,-2,-3,-4,3,2,1]))