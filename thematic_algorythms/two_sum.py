"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""

def twoSum(nums: list[int], target: int) -> list[int]:
    num_map = {}
    
    for i, num in enumerate(nums):
        complement = target - num  # find the complement to the current num
        
        if complement in num_map:  # if complement already exists in num_map, solution found
            return [num_map[complement], i]
        
        num_map[num] = i  # if not, store the current num and its index for future reference
        
twoSum([1, 2, 3, 4, 5], 5)

"""
В чем суть решения:

- complement — это дополнение для текущего числа, т.е. число, которое, если найти в словаре, в сумме с текущим числом даст нужный target.
- С помощью enumerate мы получаем индекс и значение текущего числа.
- В словаре num_map храним все элементы, которые мы уже встретили, с их индексами.
- Для каждого числа вычисляем его complement (target - num). Если complement уже есть в словаре, значит, мы нашли пару чисел, которые в сумме дают target, и возвращаем их индексы.
- Если complement еще нет в словаре, добавляем текущее число в num_map для использования в будущих итерациях.

Пространственная сложность: O(N), так как в худшем случае мы храним все элементы в словаре.
Временная сложность: O(N), так как каждый элемент проверяется и добавляется в словарь один раз.
"""
