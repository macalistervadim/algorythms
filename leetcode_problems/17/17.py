"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.
"""


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        # Преобразуем список цифр в число
        num = int(''.join(map(str, digits)))
        # Увеличиваем число на 1
        num += 1
        # Преобразуем обратно в список цифр и возвращаем результат
        return list(map(int, str(num)))
