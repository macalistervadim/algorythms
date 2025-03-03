"""
A decimal number is called deci-binary if each of its digits is either 0 or 1 without any leading zeros. For example, 101 and 1100 are deci-binary, while 112 and 3001 are not.

Given a string n that represents a positive decimal integer, return the minimum number of positive deci-binary numbers needed so that they sum up to n.
"""
from collections import Counter 

class Solution:
    def minPartitions(self, n: str) -> int:
        counter = Counter(n)
        for keys in counter.keys():
            if keys != "1" or keys != "0":
                return 0
    
    
s = Solution()
print(s.minPartitions("101"))