"""
Найдите общий предлог у слов

find() ищет подстроку в другой строке и возвращает индекс если она там есть
"""


def longestCommonPrefix(strs: list[str]) -> str:
    if not strs:
        return ""

    prefix = strs[0]

    for s in strs[1:]:
        while s.find(prefix) != 0:
            prefix = prefix[:-1]
            print(prefix)
            if not prefix:
                return ""

    return prefix


print(longestCommonPrefix(["flower", "flow", "flight"]))
