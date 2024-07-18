"""
Нахождение элемента большинства
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_len = len(nums)%2
        for num in nums:
            if nums.count(num) > num_len:
                return num



solu = Solution()
print(solu.majorityElement([3,2,3]))