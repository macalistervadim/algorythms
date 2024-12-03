"""
Given two strings s and t, return true if t is an
anagram
 of s, and false otherwise.
"""
from collections import Counter


def anagram(s1, s2):
    return Counter(s1) == Counter(s2)

def anagram_analog(s1, s2):
    return sorted(s1) == sorted(s2)

print(anagram("anagram", "naagaram"))