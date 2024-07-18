import typing


class Solution:
    def searchInsert(self, nums: typing.List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while high >= low:
            middle = (low+high) // 2
            guest = nums[middle]

            print(f"Нижняя граница: {low}")
            print(f"Верхняя граница: {high}")
            print(f"Середина: {middle}")
            print(f"Нашли число: {guest}")

            if guest == target:
                return middle
            elif guest > target:
                high = middle - 1
            else:
                low = middle + 1

        return low

        


sol = Solution()
print(sol.searchInsert(nums = [1,3,5,6], target = 1))

        