"""
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

Example 1:

Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.
"""

from collections import Counter


def sol(s):
    print((s+s)[1:-1])
    return s in (s + s)[1:-1]


print(sol("abcabc"))