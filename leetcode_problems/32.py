"""
Given a string s, find the length of the longest substring without duplicate characters.
"""

def lengthOfLongestSubstring(s: str) -> int:
    char_set = set()  # 0(n) 
    left = 0
    max_len = 0

    for right in range(len(s)):  # O(n)
        while s[right] in char_set:  # 0(1)
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])  # O(1)
        max_len = max(max_len, right - left + 1) 

    return max_len

print(lengthOfLongestSubstring("abcde"))

# Time-Complexity: O(n)
# Memory-Complexity: O(n)
    
print(lengthOfLongestSubstring("pwwkew"))

