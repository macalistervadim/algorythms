"""

Необходимо сравнить, есть ли дубликаты в списке, если есть - то вернуть True, если нет - False

В данной задаче пытался решить при помощи set() - но такое решение оказывается верным лишь в данном случае,
ведь мы сравниваем длинны двух коллекций, а не сами элементы (а сравнить list с set мы не можем, ибо set это неупорядоченная структура данных)

"""


class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        sol = {}
        for i in nums:
            if i not in sol:
                sol[i] = 1
            else:
                return True
        return False


a = Solution()
print(a.containsDuplicate(nums=[1, 2, 3, 4]))
