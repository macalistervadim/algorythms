"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
"""

def mergeAlternately(self, word1: str, word2: str) -> str:
    result = []
    i = j = 0
    while i < len(word1) and j < len(word2):
        result.append(word1[i])
        result.append(word2[j])
        i += 1; j += 1

    result.extend(word1[i:]); result.extend(word2[j:])

    return ''.join(result)

