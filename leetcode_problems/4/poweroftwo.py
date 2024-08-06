"""
Необходимо найти является ли число степенью двойки
"""


class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False

        while n > 1:
            if n % 2 != 0:
                return False
            n //= 2

        return True


ofof = Solution()
ofof.isPowerOfTwo(5)
