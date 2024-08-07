class Solution:
    def sumOfUnique(self, nums: list[int]) -> int:
        result = 0
        dct = {}
        print(dct)
        for i in nums:
            if i not in dct:
                dct[i] = 1
            else:
                dct[i] += 1
        
        for j in dct:
            if dct[j] == 1:
                result += j
            
        
        return result
    

s = Solution()
print(s.sumOfUnique([1,1,1,1,1]))