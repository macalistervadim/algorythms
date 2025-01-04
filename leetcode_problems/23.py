"""
An array is monotonic if it is either monotone increasing or monotone decreasing.

An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].

Given an integer array nums, return true if the given array is monotonic, or false otherwise.
"""



def isMonotonic(self, nums: list[int]) -> bool:
    direction = 0 # 0 - unknown, 1 - increasing, -1 - decreasing

    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]: # increasing
            if direction == 0:
                direction = 1
            elif direction == -1:
                return False
        elif nums[i] < nums[i - 1]: # decreasing
            if direction == 0:
                direction = -1
            elif direction == 1:
                return False

    return True