"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
"""
from collections import defaultdict


def anagram(strs):
    anagram_map = defaultdict(list)

    for word in strs:
        sorted_word = ''.join(sorted(word))
        anagram_map[sorted_word].append(word)

    return list(anagram_map.values())
        
    

print(anagram(["eat","tea","tan","ate","nat","bat"]))