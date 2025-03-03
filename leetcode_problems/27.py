"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums = {}
        
        for i, num in enumerate(nums):
            target_num = target - num
            
            if target_num in nums:
                return [nums[target_num], i]
            
            nums[num] = i
    
    
s = Solution()
print(s.twoSum([1, 2, 3], 3))