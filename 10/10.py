"""
Дан двумерный список, необходимо найти, какой из подсписков имеет наибольшую сумму
"""


class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        maxcount = 0
        for i in accounts:
            if maxcount < sum(i):
                maxcount = sum(i)
        return maxcount

s = Solution()
print(s.maximumWealth(accounts = [[1,5],[7,3],[3,5]]))