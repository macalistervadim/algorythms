from collections import Counter

class Solution:
    def romanToInt(self, s: str) -> int:
        counter = Counter(s)
        for i in counter.keys():
            print(i)
            
s = Solution()
s.romanToInt("III")