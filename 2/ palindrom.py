"""
Нахождение палиндрома
"""

class Solution(object):
    def firstPalindrome(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        returned = ""
        for word in words:
            if word[0:] == word[::-1]:
                returned += word
                break
        print(returned)

sol = Solution()
sol.firstPalindrome(["notapalindrome","racecar"])