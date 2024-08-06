class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for i in s:
            if s.count(i) <= 1:
                result = s.index(i)
                break
            
        if result == 0:
            return -1
        else:
            return result

            
a = Solution()
print(a.firstUniqChar("leetcode"))

