def summ(nums: list[int]) -> int:
    if nums == []:
        return 0
    else:
        return 1 + summ(nums[1:])
    
print(summ([1, 5, 7, 10]))

lst = [1, 4, 5, 6, 10]
print(lst[1:])